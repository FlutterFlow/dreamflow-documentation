# Documentation Update Workflow

This guide explains the best strategies for updating your Firestore documentation index when docs change.

## 🎯 **Recommended Strategy: Incremental Updates**

For most documentation updates, use **incremental updates** because they are:
- ⚡ **Faster** (only processes changed files)
- 💰 **Cost-effective** (fewer Firestore API calls and OpenAI embedding requests)
- 🔄 **Efficient** (maintains existing records)
- 🛡️ **Safer** (less risk of data loss)

## 📋 **Usage Options**

### 1. **Incremental Update (Recommended)**
```bash
python update_docs.py --mode incremental
```
- Only processes files that have changed
- Deletes records for removed files
- Updates records for modified files
- Keeps unchanged records intact

### 2. **Full Refresh (When Needed)**
```bash
python update_docs.py --mode full
```
- Deletes ALL existing records
- Processes ALL documentation files
- Use when you need a complete rebuild

## 🔍 **How Change Detection Works**

The script tracks file changes using:
- **MD5 hashes** of file content
- **Modification timestamps**
- **File sizes**
- **State persistence** in `docs_state.json`

## 📊 **When to Use Each Mode**

### Use **Incremental** when:
- ✅ Regular documentation updates
- ✅ Adding new pages
- ✅ Editing existing content
- ✅ Minor structural changes
- ✅ Daily/weekly updates

### Use **Full Refresh** when:
- 🔄 Major restructuring
- 🔄 Changing chunking logic
- 🔄 Schema changes in metadata
- 🔄 After long periods without updates
- 🔄 Troubleshooting index issues


## 📈 **Performance Comparison**

| Mode | Speed | Firestore Calls | OpenAI Calls | Risk | Use Case |
|------|-------|------------------|---------------|------|----------|
| **Incremental** | ⚡ Fast | 🟢 Low | 🟢 Low | 🟢 Safe | Regular updates |
| **Full Refresh** | 🐌 Slow | 🔴 High | 🔴 High | 🟡 Medium | Major changes |

## 🛠️ **Troubleshooting**

### If incremental updates seem inconsistent:
```bash
python update_docs.py --mode full
```

### If you need to reset state tracking:
```bash
rm docs_state.json
python update_docs.py --mode incremental
```

### If specific files aren't updating:
```bash
# Check the state file
cat docs_state.json
```

## 📝 **Best Practices**

1. **Run incremental updates frequently** (daily/weekly)
2. **Use full refresh sparingly** (monthly/quarterly)
3. **Monitor the state file** for consistency
4. **Test changes** in a staging environment first
5. **Keep backups** of your Firestore data

## 🔧 **Configuration**

You can modify these settings in the script:
- `REPO_FOLDER`: Documentation directory
- `STATE_FILE`: Change tracking file
- `BATCH_SIZE`: Firestore upload batch size
- `MAX_CHUNK_SIZE`: Maximum chunk size
- `FIRESTORE_COLLECTION`: Firestore collection name (default: "knowledge_base")
- `OPENAI_EMBEDDING_MODEL`: OpenAI embedding model (default: "text-embedding-3-small")

## 🔐 **Environment Variables**

The script requires the following environment variables:

### Required Variables
- `FIRESTORE_PROJECT_ID`: Your Google Cloud Firestore project ID
- `FIRESTORE_CREDENTIALS_JSON`: Service account credentials as JSON string
- `OPENAI_API_KEY`: Your OpenAI API key for generating embeddings

### Example Setup
```bash
export FIRESTORE_PROJECT_ID="your-project-id"
export FIRESTORE_CREDENTIALS_JSON='{"type": "service_account", "project_id": "your-project-id", ...}'
export OPENAI_API_KEY="sk-your-openai-key"
```

## 🔥 **Firestore Collection Structure**

The script creates documents in the `knowledge_base` collection with this structure:

```json
{
  "id": "filename-header-0",
  "text": "Documentation content...",
  "embedding": [0.1, 0.2, ...],
  "chunk_index": 0,
  "source_file": "get-started/quickstart.md",
  "header": "Getting Started",
  "docs_url": "https://docs.dreamflow.com/get-started/quickstart#getting-started",
  "category": "Dreamflow Documentation",
  "created_at": "2024-01-01T00:00:00Z"
}
```

## 📊 **Monitoring**

The script provides detailed logging:
- Files detected as changed
- Number of chunks processed
- OpenAI embedding generation progress
- Firestore upload progress
- Error handling

Monitor these logs to ensure updates are working correctly.

## 🚀 **GitHub Actions Deployment**

The repository includes automated deployment workflows:

### Dev Deployment
- **Trigger**: Push to `main` or `develop` branches
- **Workflow**: `.github/workflows/update-docs-dev.yml`
- **Environment**: Dev Firestore project
- **Secrets Required**:
  - `DEV_FIRESTORE_PROJECT_ID`
  - `DEV_FIRESTORE_CREDENTIALS_JSON`
  - `OPENAI_API_KEY`

### Prod Deployment
- **Trigger**: Push to `main` branch or tag creation
- **Workflow**: `.github/workflows/update-docs-prod.yml`
- **Environment**: Prod Firestore project
- **Secrets Required**:
  - `PROD_FIRESTORE_PROJECT_ID`
  - `PROD_FIRESTORE_CREDENTIALS_JSON`
  - `OPENAI_API_KEY`

### Setting Up GitHub Secrets

1. Go to your repository Settings → Secrets and variables → Actions
2. Add the following secrets:
   - `DEV_FIRESTORE_PROJECT_ID`: Your dev Firestore project ID
   - `DEV_FIRESTORE_CREDENTIALS_JSON`: Complete service account JSON
   - `PROD_FIRESTORE_PROJECT_ID`: Your prod Firestore project ID
   - `PROD_FIRESTORE_CREDENTIALS_JSON`: Complete service account JSON
   - `OPENAI_API_KEY`: Your OpenAI API key

## 💰 **Cost Optimization**

### Firestore Costs
- **Document writes**: ~$0.18 per 100K operations
- **Document reads**: ~$0.06 per 100K operations
- **Storage**: ~$0.18 per GB per month

### OpenAI Costs
- **text-embedding-3-small**: ~$0.02 per 1M tokens
- **Typical documentation**: ~100-500 tokens per chunk

### Best Practices
- Use incremental updates to minimize API calls
- Batch operations to reduce Firestore write costs
- Monitor usage in Google Cloud Console
- Set up billing alerts for cost control
