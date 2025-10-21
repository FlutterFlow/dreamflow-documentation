#!/usr/bin/env python3
"""
Enhanced script for incremental documentation updates to Pinecone.

This script supports:
1. Incremental updates (only changed files)
2. Full refresh (delete all and regenerate)
3. File change detection
4. Selective file processing
"""

import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional

# Configuration Constants
class Config:
    """Configuration constants for the documentation updater."""
    REPO_FOLDER = "./docs"
    OUTPUT_FILE = "documentation_rag_chunks.json"
    STATE_FILE = "docs_state.json"
    MAX_CHUNK_SIZE = 500
    BATCH_SIZE = 50
    DELETE_BATCH_SIZE = 100
    BASE_URL = "https://docs.dreamflow.com"
    
    # Pinecone Configuration (must be set via environment variables)
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    PINECONE_INDEX_HOST = os.getenv("PINECONE_INDEX_HOST")

# Utility Functions
def install_dependencies() -> None:
    """Install required Python packages."""
    print("📦 Installing required dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pinecone"])
        print("✅ Dependencies installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        sys.exit(1)


def get_file_hash(file_path: str) -> Optional[str]:
    """Get MD5 hash of file content for change detection.
    
    Args:
        file_path: Path to the file to hash
        
    Returns:
        MD5 hash as hex string, or None if file cannot be read
    """
    try:
        with open(file_path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    except (IOError, OSError):
        return None


def load_file_state() -> Dict[str, Dict[str, str]]:
    """Load previous file states for change detection.
    
    Returns:
        Dictionary mapping file paths to their state information
    """
    if os.path.exists(Config.STATE_FILE):
        try:
            with open(Config.STATE_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    return {}


def save_file_state(state: Dict[str, Dict[str, str]]) -> None:
    """Save current file states.
    
    Args:
        state: Dictionary of file states to save
    """
    with open(Config.STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)

# File Change Detection
def get_changed_files() -> Tuple[List[str], List[str], Dict[str, str]]:
    """Detect which files have changed since last run.
    
    Returns:
        Tuple of (changed_files, deleted_files, current_hashes)
    """
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

# Markdown Processing
def clean_markdown_content(md_text: str) -> str:
    """Remove HTML content and images from markdown text.
    
    Args:
        md_text: Raw markdown text
        
    Returns:
        Cleaned markdown text
    """
    # Remove HTML tags
    md_text = re.sub(r'<[^>]+>', '', md_text)
    
    # Remove image references (both markdown and HTML formats)
    md_text = re.sub(r'!\[.*?\]\(.*?\)', '', md_text)  # ![alt](url)
    md_text = re.sub(r'<img[^>]*>', '', md_text)  # <img> tags
    
    # Remove HTML entities and clean up whitespace
    md_text = re.sub(r'&[^;]+;', '', md_text)
    md_text = re.sub(r'\n\s*\n\s*\n', '\n\n', md_text)  # Clean up multiple newlines
    
    return md_text.strip()


def split_by_headers(md_text: str) -> List[Dict[str, str]]:
    """Split markdown text by headers to create navigatable chunks.
    
    Args:
        md_text: Markdown text to split
        
    Returns:
        List of chunks with header and content
    """
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
    """Generate a URL for a specific chunk based on file path and header.
    
    Args:
        source_file: Relative path to the source file
        header: Header text for the chunk
        md_content: Markdown content to extract slug from frontmatter
        
    Returns:
        Full URL for the chunk
    """
    # Try to extract slug from frontmatter
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
    """Extract slug from markdown frontmatter.
    
    Args:
        md_content: Markdown content with frontmatter
        
    Returns:
        Slug path or empty string if not found
    """
    if not md_content:
        return ""
    
    # Look for slug in frontmatter
    slug_match = re.search(r'^slug:\s*(.+)$', md_content, re.MULTILINE)
    if slug_match:
        return slug_match.group(1).strip()
    
    return ""


def process_specific_files(file_paths: List[str]) -> List[Dict[str, any]]:
    """Process only specific files and return records for Pinecone.
    
    Args:
        file_paths: List of file paths to process
        
    Returns:
        List of records ready for Pinecone upload
    """
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

# Pinecone Operations
def _get_pinecone_index():
    """Get initialized Pinecone index."""
    # Validate environment variables
    if not Config.PINECONE_API_KEY:
        print("❌ PINECONE_API_KEY environment variable is not set")
        sys.exit(1)
    if not Config.PINECONE_INDEX_HOST:
        print("❌ PINECONE_INDEX_HOST environment variable is not set")
        sys.exit(1)
    
    try:
        from pinecone import Pinecone
        pc = Pinecone(api_key=Config.PINECONE_API_KEY)
        return pc.Index(host=Config.PINECONE_INDEX_HOST)
    except ImportError:
        print("❌ Pinecone client not installed. Please run: pip install pinecone")
        sys.exit(1)


def delete_records_from_pinecone(source_files: List[str]) -> None:
    """Delete records from Pinecone for specific source files.
    
    Args:
        source_files: List of source file paths to delete records for
    """
    print("🗑️ Deleting records from Pinecone...")
    
    try:
        index = _get_pinecone_index()
        
        for source_file in source_files:
            # Query to find records with this source file
            query_response = index.query(
                vector=[0] * 1024,  # Dummy vector for metadata filtering (matches index dimension)
                top_k=10000,  # Large number to get all matches
                include_metadata=True,
                filter={"source_file": source_file}
            )
            
            if query_response.matches:
                ids_to_delete = [match.id for match in query_response.matches]
                print(f"  🗑️ Deleting {len(ids_to_delete)} records for {source_file}")
                
                # Delete in batches
                for i in range(0, len(ids_to_delete), Config.DELETE_BATCH_SIZE):
                    batch_ids = ids_to_delete[i:i+Config.DELETE_BATCH_SIZE]
                    index.delete(ids=batch_ids)
        
        print("✅ Deletion completed")
        
    except Exception as e:
        print(f"❌ Error deleting from Pinecone: {e}")


def upload_to_pinecone(chunks: List[Dict[str, any]]) -> None:
    """Upload processed chunks to Pinecone.
    
    Args:
        chunks: List of chunk records to upload
    """
    print("🌲 Uploading to Pinecone...")
    
    try:
        index = _get_pinecone_index()
        
        # Convert chunks to Pinecone format
        records = _convert_chunks_to_pinecone_records(chunks)
        
        # Upload in batches
        total_uploaded = 0
        for i in range(0, len(records), Config.BATCH_SIZE):
            batch = records[i:i+Config.BATCH_SIZE]
            index.upsert_records("__default__", batch)
            total_uploaded += len(batch)
            print(f"  📤 Uploaded batch {i//Config.BATCH_SIZE + 1}/{(len(records)-1)//Config.BATCH_SIZE + 1} ({total_uploaded}/{len(records)} records)")

        print(f"✅ Successfully uploaded {len(records)} records to Pinecone")
        
    except Exception as e:
        print(f"❌ Error uploading to Pinecone: {e}")
        sys.exit(1)


def _convert_chunks_to_pinecone_records(chunks: List[Dict[str, any]]) -> List[Dict[str, any]]:
    """Convert chunk records to Pinecone format."""
    records = []
    for chunk in chunks:
        record = {
            "_id": chunk["id"],
            "text": chunk["text"],  # Pinecone will embed this
            "chunk_index": chunk["metadata"]["chunk_index"],
            "source_file": chunk["metadata"]["source_file"],
            "header": chunk["metadata"]["header"],
            "docs_url": chunk["metadata"]["docs_url"]
        }
        records.append(record)
    return records

# Main Update Functions
def incremental_update() -> None:
    """Perform incremental update - only process changed files."""
    print("🔄 Starting incremental update...")
    
    changed_files, deleted_files, current_hashes = get_changed_files()
    
    if not changed_files and not deleted_files:
        print("✅ No changes detected. Index is up to date!")
        return
    
    # Delete records for deleted files AND changed files
    files_to_clean = deleted_files + [os.path.relpath(f, Config.REPO_FOLDER) for f in changed_files]
    if files_to_clean:
        delete_records_from_pinecone(files_to_clean)
    
    # Process changed files
    if changed_files:
        chunks = process_specific_files(changed_files)
        #_save_chunks_to_json(chunks)
        upload_to_pinecone(chunks)
        
    
    # Save state only after successful processing
    state_to_save = {rel_path: {'hash': hash_value} for rel_path, hash_value in current_hashes.items()}
    save_file_state(state_to_save)
    
    print("✅ Incremental update completed!")


def full_refresh() -> None:
    """Perform full refresh - delete all and regenerate."""
    print("🔄 Starting full refresh...")
    
    try:
        index = _get_pinecone_index()
        
        # Delete all records
        print("🗑️ Deleting all existing records...")
        index.delete(delete_all=True)
        
        # Process all files
        print("📄 Processing all files...")
        all_files = _get_all_markdown_files()
        
        chunks = process_specific_files(all_files)
        #_save_chunks_to_json(chunks)
        upload_to_pinecone(chunks)
    
        
        # Save current file hashes for future incremental updates
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

# Only used for debugging
def _save_chunks_to_json(chunks: List[Dict[str, any]]) -> None:
    """Save processed chunks to JSON file for inspection.
    
    Args:
        chunks: List of chunk records to save
    """
    try:
        with open(Config.OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(chunks, f, indent=2, ensure_ascii=False)
        print(f"📄 Saved {len(chunks)} chunks to {Config.OUTPUT_FILE}")
    except Exception as e:
        print(f"⚠️ Error saving chunks to JSON: {e}")

# Main Entry Point
def main() -> None:
    """Main function with command line options."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Update Dreamflow documentation in Pinecone',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python update_docs.py                    # Incremental update (default)
  python update_docs.py --mode full        # Full refresh
  python update_docs.py --install-deps     # Install dependencies first
        """
    )
    
    parser.add_argument(
        '--mode', 
        choices=['incremental', 'full'], 
        default='incremental',
        help='Update mode: incremental (default) or full refresh'
    )
    parser.add_argument(
        '--install-deps', 
        action='store_true',
        help='Install dependencies before running'
    )
    
    args = parser.parse_args()
    
    print("🚀 Starting Dreamflow Documentation Update")
    print("=" * 50)
    
    if args.install_deps:
        install_dependencies()
    
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
