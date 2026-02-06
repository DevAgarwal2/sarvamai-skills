# Sarvam AI Document Intelligence Skill Template

## Overview
This template helps you create skills that use Sarvam AI's Document Intelligence API to extract text from PDFs and images in 23 languages (22 Indian + English).

**Two Processing Modes:**
1. **Direct Processing** - For small PDFs (≤5 pages)
2. **Batch Processing** - For large PDFs (any size, splits into chunks)

## API Information

**Model:** sarvam-vision (3B parameter Vision Language Model)  
**SDK:** `sarvamai` Python library  
**Client:** `client.document_intelligence`

## Supported Input Formats

- PDF documents (any size)
- ZIP archives (containing JPG/PNG images)

**Note:** Individual PNG/JPG files must be packaged in a ZIP archive

## Output Formats (delivered as ZIP)

- **Markdown (md)**: Clean text with preserved structure (default)
- **HTML**: Structured output with tables and formatting

**Note:** JSON format is NOT supported by the API. Only "html" and "md" are valid output formats.

The output is always delivered as a ZIP file containing the extracted content.

## Processing Strategies by PDF Size

### Small PDFs (≤5 pages)
- **Strategy**: Direct processing (no splitting)
- **File**: `examples/document_intelligence.py`
- **Output**: `filename_output.md` or `filename_output.html`

### Large PDFs (>5 pages)
- **Strategy**: Batch processing with automatic chunking
- **File**: `examples/document_intelligence_batch.py`
- **Output**: `filename_merged.md` (chunks merged in order)
- **Examples**:
  - 10 pages → 2 chunks (5+5)
  - 25 pages → 5 chunks (5+5+5+5+5)
  - 100 pages → 20 chunks (20×5 pages)

## Supported Languages (23)

All 22 official Indian languages plus English:

### Core 11 Languages

| Language | Code | Script |
|----------|------|--------|
| Hindi | hi-IN | Devanagari |
| Bengali | bn-IN | Bengali |
| Tamil | ta-IN | Tamil |
| Telugu | te-IN | Telugu |
| Marathi | mr-IN | Devanagari |
| Gujarati | gu-IN | Gujarati |
| Kannada | kn-IN | Kannada |
| Malayalam | ml-IN | Malayalam |
| Odia | od-IN | Odia |
| Punjabi | pa-IN | Gurmukhi |
| English | en-IN | Latin |

### Extended 12 Languages

| Language | Code | Script |
|----------|------|--------|
| Assamese | as-IN | Assamese |
| Urdu | ur-IN | Perso-Arabic |
| Sanskrit | sa-IN | Devanagari |
| Nepali | ne-IN | Devanagari |
| Konkani | kok-IN | Devanagari |
| Maithili | mai-IN | Devanagari |
| Sindhi | sd-IN | Devanagari/Arabic |
| Kashmiri | ks-IN | Perso-Arabic |
| Dogri | doi-IN | Devanagari |
| Manipuri | mni-IN | Meetei Mayek |
| Bodo | brx-IN | Devanagari |
| Santali | sat-IN | Ol Chiki |

## SDK Workflow

Document Intelligence uses a simple object-oriented workflow:

1. **Create Job** → `client.document_intelligence.create_job()`
2. **Upload File** → `job.upload_file()`
3. **Start Processing** → `job.start()`
4. **Wait for Completion** → `job.wait_until_complete()`
5. **Get Metrics** → `job.get_page_metrics()`
6. **Download Output** → `job.download_output()`

## Python SDK Example (Complete Workflow)

```python
import os
from sarvamai import SarvamAI

# Initialize client
client = SarvamAI(api_subscription_key=os.getenv("SARVAM_API_KEY"))

# Step 1: Create a document intelligence job
job = client.document_intelligence.create_job(
    language="hi-IN",
    output_format="md"
)
print(f"Job created: {job.job_id}")

# Step 2: Upload document
job.upload_file("document.pdf")
print("File uploaded")

# Step 3: Start processing
job.start()
print("Job started")

# Step 4: Wait for completion
status = job.wait_until_complete()
print(f"Job completed with state: {status.job_state}")

# Step 5: Get processing metrics
metrics = job.get_page_metrics()
print(f"Page metrics: {metrics}")

# Step 6: Download output (ZIP file containing the processed document)
job.download_output("./output.zip")
print("Output saved to ./output.zip")
```

## DocumentIntelligenceJob Object

When you call `create_job()`, it returns a `DocumentIntelligenceJob` object with these methods:

### Properties
- `job_id` - Unique job identifier
- `language` - Document language code
- `output_format` - Output format (html or md only)

### Methods
- `upload_file(file_path)` - Upload PDF or ZIP file
- `start()` - Begin document processing
- `wait_until_complete()` - Block until processing completes, returns status
- `get_status()` - Get current job status
- `get_page_metrics()` - Get detailed page processing metrics
- `download_output(output_path)` - Download processed output as ZIP

## Job States

The `wait_until_complete()` method returns a status object with `job_state`:

- `Accepted` - Job created, awaiting file upload
- `Pending` - File uploaded, waiting to start  
- `Running` - Processing in progress
- `Completed` - All pages processed successfully
- `PartiallyCompleted` - Some pages succeeded, some failed
- `Failed` - All pages failed or job-level error

## Batch Processing for Large PDFs

For PDFs with more than 5 pages, use the batch processing workflow:

### Batch Processing SDK Example

```python
from document_intelligence_batch import process_large_pdf

# Automatically handles PDFs of any size
output = process_large_pdf(
    input_pdf="large_document.pdf",  # Any size: 10, 25, 100+ pages
    language="hi-IN",
    output_format="md",  # or "html"
    pages_per_chunk=5,   # Recommended chunk size
    cleanup=True,        # Remove temporary files
    keep_chunks=False    # Don't keep intermediate PDFs
)
# Output: large_document_merged.md
```

### How Batch Processing Works

1. **PDF Analysis**: Checks total page count
2. **Strategy Selection**:
   - ≤5 pages → Direct processing (no splitting)
   - >5 pages → Split into 5-page chunks
3. **Chunking**: Splits PDF into smaller files (e.g., 25 pages → 5 chunks)
4. **Processing**: Each chunk processed via Document Intelligence API
5. **Merging**: All outputs merged in correct order (Chunk 1, 2, 3...)
6. **Cleanup**: Removes temporary files (optional)

### Batch Processing Examples

**10-page PDF:**
```python
output = process_large_pdf("report.pdf", language="en-IN")
# → 2 chunks (5+5 pages)
# → Output: report_merged.md
```

**25-page PDF:**
```python
output = process_large_pdf("book.pdf", language="hi-IN", output_format="html")
# → 5 chunks (5+5+5+5+5 pages)
# → Output: book_merged.html
```

**100-page PDF:**
```python
output = process_large_pdf("thesis.pdf", language="ta-IN", pages_per_chunk=5)
# → 20 chunks (20×5 pages)
# → Output: thesis_merged.md
```

### Batch Processing Requirements

```bash
pip install PyPDF2>=3.0.0
```

See `examples/document_intelligence_batch.py` for complete implementation.

## Output Structure

After downloading and extracting the ZIP file:

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
**Solution:** HTML output preserves table structure for programmatic parsing  
**Recommended Format:** HTML

### 4. Historical Archives
**Challenge:** Native Indic script support  
**Solution:** All 23 Indian languages supported  
**Recommended Format:** Markdown

## Format Comparison

| Format | Best For | Pros | Cons |
|--------|----------|------|------|
| **Markdown** | Text documents, articles | Clean, readable, easy to process | Basic table support |
| **HTML** | Complex tables, forms, data extraction | Rich formatting, preserves layout, structured tables | More verbose |

## Best Practices

1. **File Preparation:**
   - PDFs should be text-based or high-quality scans
   - Images in ZIP should be 300+ DPI for best OCR
   - Maximum file size: 200 MB
   - Maximum pages: 500

2. **Error Handling:**
   - Check `status.job_state` for "Failed"
   - Handle exceptions from upload/download operations
   - Verify file exists before uploading

3. **Format Selection:**
   - Use Markdown for simple text documents
   - Use HTML for documents with complex tables or data extraction needs
   - JSON format is NOT supported by the API

4. **Language Selection:**
   - Always specify correct language for better OCR accuracy
   - Language setting optimizes text recognition for that script

## Complete Example with Error Handling

```python
import os
from sarvamai import SarvamAI

def process_document_safe(file_path: str, language: str = "en-IN", output_format: str = "md"):
    """Process document with error handling."""
    try:
        # Initialize client
        client = SarvamAI(api_subscription_key=os.getenv("SARVAM_API_KEY"))
        
        # Create job
        job = client.document_intelligence.create_job(
            language=language,
            output_format=output_format
        )
        print(f"Job created: {job.job_id}")
        
        # Upload file
        job.upload_file(file_path)
        print("File uploaded successfully")
        
        # Start processing
        job.start()
        print("Processing started")
        
        # Wait for completion
        status = job.wait_until_complete()
        
        if status.job_state == "Failed":
            print(f"Processing failed!")
            return None
        
        print(f"Processing completed: {status.job_state}")
        
        # Get metrics
        metrics = job.get_page_metrics()
        print(f"Pages: {metrics}")
        
        # Download output
        output_file = f"{os.path.splitext(file_path)[0]}_output.zip"
        job.download_output(output_file)
        print(f"Output saved to: {output_file}")
        
        return output_file
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
    except Exception as e:
        print(f"Error: {e}")
    
    return None

# Usage
result = process_document_safe("document.pdf", language="hi-IN", output_format="md")
```

## Resources

- [API Documentation](https://docs.sarvam.ai/api-reference-docs/document-intelligence)
- [Python SDK](https://pypi.org/project/sarvamai/)
- [Dashboard](https://dashboard.sarvam.ai)
- [Sarvam Vision Model Info](https://docs.sarvam.ai/api-reference-docs/getting-started/models/sarvam-vision)
