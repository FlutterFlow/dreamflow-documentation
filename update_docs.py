#!/usr/bin/env python3
import hashlib
import json
import os
import re
import subprocess
import sys
from typing import Dict, List, Tuple, Optional
import openai
from google.cloud import firestore
from google.oauth2 import service_account

# Configuration Constants
class Config:
    """Configuration constants for the documentation updater."""
    REPO_FOLDER = "./docs"
    STATE_FILE = "docs_state.json"
    MAX_CHUNK_SIZE = 500
    BATCH_SIZE = 50
    DELETE_BATCH_SIZE = 20
    BASE_URL = "https://docs.dreamflow.com"
    
    # Firestore Configuration (must be set via environment variables)
    FIRESTORE_PROJECT_ID = os.getenv("FIRESTORE_PROJECT_ID")
    FIRESTORE_COLLECTION = "knowledge_base"
    FIRESTORE_CREDENTIALS_JSON = os.getenv("FIRESTORE_CREDENTIALS_JSON")
    
    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_EMBEDDING_MODEL = "text-embedding-3-small"


def get_file_hash(file_path: str) -> Optional[str]:
    """Get MD5 hash of file content for change detection."""
    try:
        with open(file_path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    except (IOError, OSError):
        return None


def load_file_state() -> Dict[str, Dict[str, str]]:
    """Load previous file states for change detection."""
    if os.path.exists(Config.STATE_FILE):
        try:
            with open(Config.STATE_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    return {}


def save_file_state(state: Dict[str, Dict[str, str]]) -> None:
    """Save current file states."""
    with open(Config.STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)
        

def get_changed_files() -> Tuple[List[str], List[str], Dict[str, str]]:
    """Detect which files have changed since last run."""
    print("🔍 Detecting changed files...")
    
    previous_state = load_file_state()
    current_hashes = {}
    changed_files = []
    new_files = []
    
    # Scan for markdown files
    for root, _, files in os.walk(Config.REPO_FOLDER):
        for filename in files:
            if _is_valid_markdown_file(filename):
                file_path = os.path.join(root, filename)
                rel_path = os.path.relpath(file_path, Config.REPO_FOLDER)
                
                current_hash = get_file_hash(file_path)
                if current_hash:
                    current_hashes[rel_path] = current_hash
                    
                    if rel_path in previous_state:
                        if previous_state[rel_path]['hash'] != current_hash:
                            changed_files.append(file_path)
                            print(f"  📝 Changed: {rel_path}")
                    else:
                        new_files.append(file_path)
                        print(f"  🆕 New: {rel_path}")
    
    # Check for deleted files
    deleted_files = _find_deleted_files(previous_state)
    
    print(f"📊 Summary: {len(changed_files)} changed, {len(new_files)} new, {len(deleted_files)} deleted")
    return changed_files + new_files, deleted_files, current_hashes


def _is_valid_markdown_file(filename: str) -> bool:
    """Check if file is a valid markdown file for processing."""
    return filename.endswith(".md") and filename != "index.md"


def _find_deleted_files(previous_state: Dict[str, Dict[str, str]]) -> List[str]:
    """Find files that were deleted since last run."""
    deleted_files = []
    for rel_path in previous_state:
        full_path = os.path.join(Config.REPO_FOLDER, rel_path)
        if not os.path.exists(full_path):
            deleted_files.append(rel_path)
            print(f"  🗑️ Deleted: {rel_path}")
    return deleted_files

def clean_markdown_content(md_text: str) -> str:
    """Remove HTML content and images from markdown text."""
    # Remove HTML tags and images
    md_text = re.sub(r'<[^>]+>', '', md_text)
    md_text = re.sub(r'!\[.*?\]\(.*?\)', '', md_text)
    md_text = re.sub(r'<img[^>]*>', '', md_text)
    
    # Clean up HTML entities and whitespace
    md_text = re.sub(r'&[^;]+;', '', md_text)
    md_text = re.sub(r'\n\s*\n\s*\n', '\n\n', md_text)
    
    return md_text.strip()


def split_by_headers(md_text: str) -> List[Dict[str, str]]:
    """Split markdown text by headers to create navigatable chunks."""
    md_text = clean_markdown_content(md_text)
    header_pattern = r'^(#{2,6})\s+(.+)$'
    lines = md_text.split('\n')
    
    chunks = []
    current_section = []
    current_header = None
    
    for line in lines:
        header_match = re.match(header_pattern, line)
        
        if header_match:
            # Save previous section
            if current_section and current_header:
                section_text = '\n'.join(current_section).strip()
                if section_text:
                    chunks.append({
                        'header': current_header,
                        'content': section_text
                    })
            
            # Start new section
            current_header = header_match.group(2).strip()
            current_section = [line]
        else:
            current_section.append(line)
    
    # Add the last section
    if current_section and current_header:
        section_text = '\n'.join(current_section).strip()
        if section_text:
            chunks.append({
                'header': current_header,
                'content': section_text
            })
    
    # If no headers found, treat entire content as one chunk
    if not chunks:
        cleaned_content = clean_markdown_content(md_text)
        if cleaned_content:
            chunks.append({
                'header': 'Introduction',
                'content': cleaned_content
            })
    
    return chunks

def generate_url_for_chunk(source_file: str, header: str, md_content: str = "") -> str:
    """Generate a URL for a specific chunk based on file path and header."""
    url_path = _extract_slug_from_frontmatter(md_content)
    
    # Fallback to file path if no slug found
    if not url_path:
        path_parts = source_file.replace('.md', '').split('/')
        if len(path_parts) >= 2:
            url_path = f"{path_parts[-2]}/{path_parts[-1]}"
        else:
            url_path = path_parts[-1]
    
    # Convert header to URL fragment (anchor)
    header_anchor = re.sub(r'[^a-zA-Z0-9\s-]', '', header.lower())
    header_anchor = re.sub(r'\s+', '-', header_anchor.strip())
    
    return f"{Config.BASE_URL}{url_path}#{header_anchor}"


def _extract_slug_from_frontmatter(md_content: str) -> str:
    """Extract slug from markdown frontmatter."""
    if not md_content:
        return ""
    
    # Look for slug in frontmatter
    slug_match = re.search(r'^slug:\s*(.+)$', md_content, re.MULTILINE)
    if slug_match:
        return slug_match.group(1).strip()
    
    return ""


def process_specific_files(file_paths: List[str]) -> List[Dict[str, any]]:
    """Process only specific files and return records for Firestore."""
    print(f"📄 Processing {len(file_paths)} specific files...")
    
    all_records = []
    
    for file_path in file_paths:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                md_content = f.read()
            
            chunks = split_by_headers(md_content)
            rel_path = os.path.relpath(file_path, Config.REPO_FOLDER)
            
            for idx, chunk_data in enumerate(chunks):
                chunk_url = generate_url_for_chunk(rel_path, chunk_data['header'], md_content)
                
                record = {
                    "id": _generate_chunk_id(file_path, chunk_data['header'], idx),
                    "text": chunk_data['content'],
                    "metadata": {
                        "source_file": rel_path,
                        "docs_url": chunk_url,
                        "category": "Dreamflow Documentation",
                        "header": chunk_data['header'],
                        "chunk_index": idx
                    }
                }
                all_records.append(record)
            
            print(f"  ✅ Processed {os.path.basename(file_path)} ({len(chunks)} header-based chunks)")
            
        except Exception as e:
            print(f"⚠️ Error reading {file_path}: {e}")

    return all_records


def _generate_chunk_id(file_path: str, header: str, index: int) -> str:
    """Generate a unique ID for a chunk."""
    filename = os.path.basename(file_path).replace('.md', '')
    header_slug = header.lower().replace(' ', '-')
    return f"{filename}-{header_slug}-{index}"


def get_openai_embedding(text: str) -> List[float]:
    """Get OpenAI embedding for text."""
    if not Config.OPENAI_API_KEY:
        print("❌ OPENAI_API_KEY environment variable is not set")
        sys.exit(1)
    
    try:
        client = openai.OpenAI(api_key=Config.OPENAI_API_KEY)
        response = client.embeddings.create(
            model=Config.OPENAI_EMBEDDING_MODEL,
            input=text
        )
        return response.data[0].embedding
    except Exception as e:
        print(f"❌ Error getting OpenAI embedding: {e}")
        sys.exit(1)


def get_firestore_client():
    """Get initialized Firestore client."""
    if not Config.FIRESTORE_PROJECT_ID:
        print("❌ FIRESTORE_PROJECT_ID environment variable is not set")
        sys.exit(1)
    
    try:
        if Config.FIRESTORE_CREDENTIALS_JSON:
            # Check if it's a file path or JSON string
            if os.path.exists(Config.FIRESTORE_CREDENTIALS_JSON):
                credentials = service_account.Credentials.from_service_account_file(Config.FIRESTORE_CREDENTIALS_JSON)
            else:
                credentials_info = json.loads(Config.FIRESTORE_CREDENTIALS_JSON)
                credentials = service_account.Credentials.from_service_account_info(credentials_info)
            
            return firestore.Client(project=Config.FIRESTORE_PROJECT_ID, credentials=credentials)
        else:
            # Use default credentials (for local development or when running in GCP)
            return firestore.Client(project=Config.FIRESTORE_PROJECT_ID)
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in FIRESTORE_CREDENTIALS_JSON: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error initializing Firestore client: {e}")
        sys.exit(1)

def delete_records_from_firestore(source_files: List[str]) -> None:
    """Delete records from Firestore for specific source files."""
    print("🗑️ Deleting records from knowledge_base collection...")
    
    try:
        db = get_firestore_client()
        collection_ref = db.collection(Config.FIRESTORE_COLLECTION)
        
        for source_file in source_files:
            query = collection_ref.where("source_file", "==", source_file)
            docs = query.stream()
            
            docs_to_delete = [doc.id for doc in docs]
            
            if docs_to_delete:
                print(f"  🗑️ Deleting {len(docs_to_delete)} records for {source_file}")
                
                for i in range(0, len(docs_to_delete), Config.DELETE_BATCH_SIZE):
                    batch = db.batch()
                    batch_ids = docs_to_delete[i:i+Config.DELETE_BATCH_SIZE]
                    for doc_id in batch_ids:
                        batch.delete(collection_ref.document(doc_id))
                    batch.commit()
        
        print("✅ Deletion completed")
        
    except Exception as e:
        print(f"❌ Error deleting from Firestore: {e}")


def upload_to_firestore(chunks: List[Dict[str, any]]) -> None:
    """Upload processed chunks to Firestore."""
    print("🔥 Uploading to knowledge_base collection...")
    
    try:
        db = get_firestore_client()
        collection_ref = db.collection(Config.FIRESTORE_COLLECTION)
        
        total_uploaded = 0
        for i in range(0, len(chunks), Config.BATCH_SIZE):
            batch = db.batch()
            batch_chunks = chunks[i:i+Config.BATCH_SIZE]
            
            for chunk in batch_chunks:
                embedding = get_openai_embedding(chunk["text"])
                
                doc_data = {
                    "id": chunk["id"],
                    "text": chunk["text"],
                    "embedding": Vector(embedding),
                    "chunk_index": chunk["metadata"]["chunk_index"],
                    "source_file": chunk["metadata"]["source_file"],
                    "header": chunk["metadata"]["header"],
                    "docs_url": chunk["metadata"]["docs_url"],
                    "category": chunk["metadata"]["category"],
                    "created_at": firestore.SERVER_TIMESTAMP
                }
                
                doc_ref = collection_ref.document(chunk["id"])
                batch.set(doc_ref, doc_data)
            
            batch.commit()
            total_uploaded += len(batch_chunks)
            print(f"  📤 Uploaded batch {i//Config.BATCH_SIZE + 1}/{(len(chunks)-1)//Config.BATCH_SIZE + 1} ({total_uploaded}/{len(chunks)} records)")

        print(f"✅ Successfully uploaded {len(chunks)} records to Firestore")
        
    except Exception as e:
        print(f"❌ Error uploading to Firestore: {e}")
        sys.exit(1)

def incremental_update() -> None:
    """Perform incremental update - only process changed files."""
    print("🔄 Starting incremental update...")
    
    changed_files, deleted_files, current_hashes = get_changed_files()
    
    if not changed_files and not deleted_files:
        print("✅ No changes detected. Index is up to date!")
        return
    
    files_to_clean = deleted_files + [os.path.relpath(f, Config.REPO_FOLDER) for f in changed_files]
    if files_to_clean:
        delete_records_from_firestore(files_to_clean)
    
    if changed_files:
        chunks = process_specific_files(changed_files)
        upload_to_firestore(chunks)
    
    state_to_save = {rel_path: {'hash': hash_value} for rel_path, hash_value in current_hashes.items()}
    save_file_state(state_to_save)
    
    print("✅ Incremental update completed!")


def full_refresh() -> None:
    """Perform full refresh - delete all and regenerate."""
    print("🔄 Starting full refresh...")
    
    try:
        db = get_firestore_client()
        collection_ref = db.collection(Config.FIRESTORE_COLLECTION)
        
        print("🗑️ Deleting all existing records from knowledge_base collection...")
        docs = collection_ref.stream()
        docs_to_delete = [doc.id for doc in docs]
        
        if docs_to_delete:
            print(f"🗑️ Deleting {len(docs_to_delete)} existing records...")
            for i in range(0, len(docs_to_delete), Config.DELETE_BATCH_SIZE):
                batch = db.batch()
                batch_ids = docs_to_delete[i:i+Config.DELETE_BATCH_SIZE]
                for doc_id in batch_ids:
                    batch.delete(collection_ref.document(doc_id))
                batch.commit()
                print(f"  📤 Deleted batch {i//Config.DELETE_BATCH_SIZE + 1}/{(len(docs_to_delete)-1)//Config.DELETE_BATCH_SIZE + 1}")
        
        all_files = _get_all_markdown_files()
        
        chunks = process_specific_files(all_files)
        upload_to_firestore(chunks)
        
        current_hashes = {}
        for file_path in all_files:
            rel_path = os.path.relpath(file_path, Config.REPO_FOLDER)
            file_hash = get_file_hash(file_path)
            if file_hash:
                current_hashes[rel_path] = {'hash': file_hash}
        
        save_file_state(current_hashes)
        
        print("✅ Full refresh completed!")
        
    except Exception as e:
        print(f"❌ Error during full refresh: {e}")
        sys.exit(1)


def _get_all_markdown_files() -> List[str]:
    """Get all markdown files in the repository."""
    all_files = []
    for root, _, files in os.walk(Config.REPO_FOLDER):
        for filename in files:
            if _is_valid_markdown_file(filename):
                all_files.append(os.path.join(root, filename))
    return all_files


def main() -> None:
    """Main function with command line options."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Update Dreamflow documentation in Firestore',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python update_docs.py                    # Incremental update (default)
  python update_docs.py --mode full        # Full refresh
        """
    )
    
    parser.add_argument(
        '--mode', 
        choices=['incremental', 'full'], 
        default='incremental',
        help='Update mode: incremental (default) or full refresh'
    )
    
    args = parser.parse_args()
    
    print("🚀 Starting Dreamflow Documentation Update")
    print("=" * 50)
    
    try:
        if args.mode == 'incremental':
            incremental_update()
        else:
            full_refresh()
        
        print("=" * 50)
        print("🎉 Documentation update completed successfully!")
        
    except KeyboardInterrupt:
        print("\n⚠️ Update cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
