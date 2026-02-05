# Sarvam AI Document Intelligence Skill Template

## Overview
This template helps you create skills that use Sarvam AI's Document Intelligence API to extract text from PDFs and images in 23 languages (22 Indian + English).

## API Information

**Base URL:** `https://api.sarvam.ai/doc-digitization/job/v1`  
**Method:** REST API (Job-based workflow)  
**Model:** sarvam-vision (3B parameter Vision Language Model)

## Supported Input Formats

- PDF documents
- ZIP archives (containing JPG/PNG images)

**Note:** Individual PNG/JPG files must be packaged in a ZIP archive

## Output Formats (delivered as ZIP)

- **Markdown (md)**: Clean text with preserved structure (default)
- **HTML**: Structured output with tables and formatting
- **JSON**: Structured data for programmatic processing

The output is always delivered as a ZIP file containing the extracted content.

## Supported Languages (23)

All 22 official Indian languages plus English:

| Language | Code | Language | Code | Language | Code |
|----------|------|----------|------|----------|------|
| Hindi | hi-IN | Assamese | as-IN | Konkani | kok-IN |
| Bengali | bn-IN | Urdu | ur-IN | Maithili | mai-IN |
| Tamil | ta-IN | Sanskrit | sa-IN | Sindhi | sd-IN |
| Telugu | te-IN | Nepali | ne-IN | Kashmiri | ks-IN |
| Marathi | mr-IN | Dogri | doi-IN | Manipuri | mni-IN |
| Gujarati | gu-IN | Bodo | brx-IN | Santali | sat-IN |
| Kannada | kn-IN | Punjabi | pa-IN | English | en-IN |
| Malayalam | ml-IN | Odia | od-IN | | |

## API Workflow

Document Intelligence uses a job-based workflow with 6 steps:

1. **Create Job** → POST `/doc-digitization/job/v1`
2. **Get Upload URL** → POST `/doc-digitization/job/v1/upload-files`
3. **Upload File** → PUT to presigned URL (Azure Blob Storage)
4. **Start Processing** → POST `/doc-digitization/job/v1/{job_id}/start`
5. **Poll for Status** → GET `/doc-digitization/job/v1/{job_id}/status`
6. **Download Output** → POST `/doc-digitization/job/v1/{job_id}/download-files`

## Endpoints

### 1. Create Job
**POST** `https://api.sarvam.ai/doc-digitization/job/v1`

**Headers:**
```
api-subscription-key: YOUR_API_KEY
Content-Type: application/json
```

**Request Body:**
```json
{
  "job_parameters": {
    "language": "hi-IN",
    "output_format": "md"
  }
}
```

**Response:**
```json
{
  "job_id": "20260205_abc123...",
  "job_state": "Accepted",
  "storage_container_type": "Azure",
  "job_parameters": {
    "language": "hi-IN",
    "output_format": "md"
  }
}
```

### 2. Get Upload URLs
**POST** `https://api.sarvam.ai/doc-digitization/job/v1/upload-files`

**Request Body:**
```json
{
  "job_id": "20260205_abc123...",
  "files": ["document.pdf"]
}
```

**Response:**
```json
{
  "job_id": "20260205_abc123...",
  "job_state": "Accepted",
  "upload_urls": {
    "document.pdf": {
      "file_url": "https://storage.sarvam.ai/...",
      "file_metadata": null
    }
  },
  "storage_container_type": "Azure"
}
```

### 3. Upload File
**PUT** to presigned URL (from step 2)

**Headers:**
```
x-ms-blob-type: BlockBlob
Content-Type: application/pdf (or application/zip)
```

**Body:** Raw file bytes

### 4. Start Processing
**POST** `https://api.sarvam.ai/doc-digitization/job/v1/{job_id}/start`

**Response:**
```json
{
  "job_id": "20260205_abc123...",
  "job_state": "Pending",
  "created_at": "2026-02-05T10:00:00Z",
  "updated_at": "2026-02-05T10:00:01Z",
  "storage_container_type": "Azure",
  "job_details": [...]
}
```

### 5. Get Job Status
**GET** `https://api.sarvam.ai/doc-digitization/job/v1/{job_id}/status`

**Response:**
```json
{
  "job_id": "20260205_abc123...",
  "job_state": "Completed",
  "created_at": "2026-02-05T10:00:00Z",
  "updated_at": "2026-02-05T10:00:30Z",
  "job_details": [{
    "total_pages": 5,
    "pages_processed": 5,
    "pages_succeeded": 5,
    "pages_failed": 0,
    "state": "Success"
  }]
}
```

**Job States:**
- `Accepted`: Job created, awaiting file upload
- `Pending`: File uploaded, waiting to start
- `Running`: Processing in progress
- `Completed`: All pages processed successfully
- `PartiallyCompleted`: Some pages succeeded, some failed
- `Failed`: All pages failed or job-level error

### 6. Download Output
**POST** `https://api.sarvam.ai/doc-digitization/job/v1/{job_id}/download-files`

**Response:**
```json
{
  "job_id": "20260205_abc123...",
  "job_state": "Completed",
  "download_urls": {
    "document.zip": {
      "file_url": "https://storage.sarvam.ai/...",
      "file_metadata": null
    }
  }
}
```

## Python Example (Complete Workflow)

```python
import os
import time
import zipfile
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SARVAM_API_KEY")
BASE_URL = "https://api.sarvam.ai/doc-digitization/job/v1"

def process_document(file_path, language="en-IN", output_format="md"):
    headers = {
        "api-subscription-key": API_KEY,
        "Content-Type": "application/json"
    }
    
    filename = os.path.basename(file_path)
    
    # Step 1: Create job
    response = requests.post(
        BASE_URL,
        headers=headers,
        json={
            "job_parameters": {
                "language": language,
                "output_format": output_format
            }
        }
    )
    job_id = response.json()["job_id"]
    print(f"Job created: {job_id}")
    
    # Step 2: Get upload URL
    upload_resp = requests.post(
        f"{BASE_URL}/upload-files",
        headers=headers,
        json={"job_id": job_id, "files": [filename]}
    )
    upload_url = upload_resp.json()["upload_urls"][filename]["file_url"]
    
    # Step 3: Upload file (with Azure Blob Storage headers)
    with open(file_path, "rb") as f:
        requests.put(
            upload_url, 
            data=f, 
            headers={"x-ms-blob-type": "BlockBlob"}
        )
    
    # Step 4: Start processing
    requests.post(f"{BASE_URL}/{job_id}/start", headers=headers)
    
    # Step 5: Poll for completion
    while True:
        status = requests.get(
            f"{BASE_URL}/{job_id}/status", 
            headers=headers
        ).json()
        
        if status["job_state"] in ["Completed", "PartiallyCompleted"]:
            break
        elif status["job_state"] == "Failed":
            raise Exception("Processing failed")
        
        time.sleep(2)
    
    # Step 6: Download output
    download_resp = requests.post(
        f"{BASE_URL}/{job_id}/download-files", 
        headers=headers
    ).json()
    
    output_file = "output.zip"
    download_url = download_resp["download_urls"]["document.zip"]["file_url"]
    
    file_response = requests.get(download_url)
    with open(output_file, "wb") as f:
        f.write(file_response.content)
    
    # Step 7: Extract ZIP
    extract_dir = "extracted_output"
    with zipfile.ZipFile(output_file, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    
    print(f"Extracted to: {extract_dir}/")
    return extract_dir

# Usage
result = process_document("document.pdf", language="hi-IN", output_format="md")
```

## cURL Example

### Create Job
```bash
curl -X POST https://api.sarvam.ai/doc-digitization/job/v1 \
  -H "api-subscription-key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "job_parameters": {
      "language": "hi-IN",
      "output_format": "md"
    }
  }'
```

### Get Upload URL
```bash
curl -X POST https://api.sarvam.ai/doc-digitization/job/v1/upload-files \
  -H "api-subscription-key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "job_id": "JOB_ID_FROM_STEP_1",
    "files": ["document.pdf"]
  }'
```

### Upload File
```bash
curl -X PUT "PRESIGNED_URL_FROM_STEP_2" \
  -H "x-ms-blob-type: BlockBlob" \
  --data-binary @document.pdf
```

### Start Processing
```bash
curl -X POST https://api.sarvam.ai/doc-digitization/job/v1/JOB_ID/start \
  -H "api-subscription-key: YOUR_API_KEY"
```

### Check Status
```bash
curl -X GET https://api.sarvam.ai/doc-digitization/job/v1/JOB_ID/status \
  -H "api-subscription-key: YOUR_API_KEY"
```

### Download Output
```bash
curl -X POST https://api.sarvam.ai/doc-digitization/job/v1/JOB_ID/download-files \
  -H "api-subscription-key: YOUR_API_KEY"
```

## Output Structure

After extracting the ZIP file:

```
extracted_output/
├── document.md          # Extracted text (Markdown format)
└── metadata/
    └── page_001.json    # Detailed OCR metadata with coordinates
```

For HTML output:
```
extracted_output/
├── document.html        # Structured HTML with formatting
└── metadata/
    └── page_001.json
```

For JSON output:
```
extracted_output/
├── document.json        # Structured JSON data
└── metadata/
    └── page_001.json
```

## Use Cases

### 1. Financial Reports
**Challenge:** Complex tables with merged cells, multi-level headers
**Solution:** Document Intelligence preserves table structure
**Recommended Format:** HTML

### 2. Legal Documents
**Challenge:** Preserving document structure and reading order
**Solution:** Maintains hierarchy and formatting
**Recommended Format:** Markdown

### 3. Invoice Processing
**Challenge:** Extracting structured data from invoices
**Solution:** JSON output for programmatic processing
**Recommended Format:** JSON

### 4. Historical Archives
**Challenge:** Native Indic script support
**Solution:** All 23 Indian languages supported
**Recommended Format:** Markdown

## Format Comparison

| Format | Best For | Pros | Cons |
|--------|----------|------|------|
| **Markdown** | Text documents, articles | Clean, readable, easy to process | Basic table support |
| **HTML** | Complex tables, forms | Rich formatting, preserves layout | More verbose |
| **JSON** | Data extraction, automation | Structured, programmatic access | Requires parsing |

## Best Practices

1. **File Preparation:**
   - PDFs should be text-based or high-quality scans
   - Images in ZIP should be 300+ DPI for best OCR
   - Maximum file size: 200 MB
   - Maximum pages: 500

2. **Azure Blob Storage Headers:**
   - Always include `x-ms-blob-type: BlockBlob` when uploading
   - This is required for Azure Blob Storage

3. **Error Handling:**
   - Handle all job states: Accepted, Pending, Running, Completed, Failed
   - Check `job_details` for per-page error information
   - Implement timeout (max 60 polling attempts recommended)

4. **Format Selection:**
   - Use Markdown for simple text documents
   - Use HTML for documents with complex tables
   - Use JSON for data extraction workflows

5. **Language Selection:**
   - Always specify correct language for better OCR accuracy
   - Language setting optimizes text recognition for that script

## Common Errors

| Error | Solution |
|-------|----------|
| 401 Unauthorized | Check API key is valid |
| 400 Bad Request | Verify file format and parameters |
| Upload fails | Include `x-ms-blob-type: BlockBlob` header |
| Job failed | Check file quality and format |
| Timeout | Document may be too large or complex |

## Resources

- [API Documentation](https://docs.sarvam.ai/api-reference-docs/document-intelligence)
- [Python SDK](https://pypi.org/project/sarvamai/)
- [Dashboard](https://dashboard.sarvam.ai)
- [Sarvam Vision Model Info](https://docs.sarvam.ai/api-reference-docs/getting-started/models/sarvam-vision)
