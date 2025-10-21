# Documentation Update Workflow

This guide explains the best strategies for updating your Pinecone documentation index when docs change.

## 🎯 **Recommended Strategy: Incremental Updates**

For most documentation updates, use **incremental updates** because they are:
- ⚡ **Faster** (only processes changed files)
- 💰 **Cost-effective** (fewer Pinecone API calls)
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

### 3. **With Dependency Installation**
```bash
python update_docs.py --mode incremental --install-deps
```

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

| Mode | Speed | API Calls | Risk | Use Case |
|------|-------|-----------|------|----------|
| **Incremental** | ⚡ Fast | 🟢 Low | 🟢 Safe | Regular updates |
| **Full Refresh** | 🐌 Slow | 🔴 High | 🟡 Medium | Major changes |

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
5. **Keep backups** of your Pinecone index

## 🔧 **Configuration**

You can modify these settings in the script:
- `REPO_FOLDER`: Documentation directory
- `STATE_FILE`: Change tracking file
- `BATCH_SIZE`: Pinecone upload batch size
- `MAX_CHUNK_SIZE`: Maximum chunk size

## 📊 **Monitoring**

The script provides detailed logging:
- Files detected as changed
- Number of chunks processed
- Upload progress
- Error handling

Monitor these logs to ensure updates are working correctly.
