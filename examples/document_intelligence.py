"""
Sarvam AI - Document Intelligence
----------------------------------
This example demonstrates how to use Sarvam AI's Document Intelligence API
to extract text from PDFs and images in 23 languages (22 Indian + English).

Model: sarvam-vision (3B parameter Vision Language Model)
API Base URL: https://api.sarvam.ai/doc-digitization/job/v1

Supported Input Formats: PDF, ZIP (containing JPG/PNG images)
Output Formats (delivered as ZIP): html, md, json

Supported languages (23): hi-IN, en-IN, bn-IN, gu-IN, kn-IN, ml-IN, mr-IN, od-IN, pa-IN, ta-IN, te-IN,
                          as-IN, ur-IN, sa-IN, ne-IN, doi-IN, brx-IN, kok-IN, mai-IN, sd-IN, ks-IN, mni-IN, sat-IN
"""

import os
import time
import zipfile
import requests
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
API_KEY = os.getenv("SARVAM_API_KEY")
BASE_URL = "https://api.sarvam.ai/doc-digitization/job/v1"


def process_document(file_path: str, language: str = "en-IN", output_format: str = "md"):
    """
    Process a document using Sarvam AI Document Intelligence API.
    
    Workflow:
    1. Create job
    2. Get upload URL
    3. Upload file
    4. Start processing
    5. Poll for completion
    6. Download and extract results
    
    Args:
        file_path: Path to PDF or ZIP file
        language: Language code (default: en-IN)
        output_format: Output format - "html", "md", or "json" (default: md)
    
    Returns:
        dict: Processing results including extracted files
    """
    if not API_KEY:
        raise ValueError("SARVAM_API_KEY not found in environment")
    
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    headers = {
        "api-subscription-key": API_KEY,
        "Content-Type": "application/json"
    }
    
    filename = file_path.name
    
    # Step 1: Create job
    print(f"Creating job for {filename}...")
    create_response = requests.post(
        BASE_URL,
        headers=headers,
        json={
            "job_parameters": {
                "language": language,
                "output_format": output_format
            }
        }
    )
    create_response.raise_for_status()
    job_data = create_response.json()
    job_id = job_data["job_id"]
    print(f"  ✓ Job created: {job_id}")
    
    # Step 2: Get upload URL
    print(f"Getting upload URL...")
    upload_response = requests.post(
        f"{BASE_URL}/upload-files",
        headers=headers,
        json={"job_id": job_id, "files": [filename]}
    )
    upload_response.raise_for_status()
    upload_data = upload_response.json()
    upload_url = upload_data["upload_urls"][filename]["file_url"]
    print(f"  ✓ Upload URL received")
    
    # Step 3: Upload file
    print(f"Uploading file...")
    with open(file_path, "rb") as f:
        requests.put(
            upload_url, 
            data=f, 
            headers={"x-ms-blob-type": "BlockBlob", "Content-Type": "application/zip"}
        )
    print(f"  ✓ File uploaded")
    
    # Step 4: Start processing
    print(f"Starting processing...")
    requests.post(f"{BASE_URL}/{job_id}/start", headers=headers)
    print(f"  ✓ Processing started")
    
    # Step 5: Poll for completion
    print(f"Waiting for completion...")
    max_attempts = 60
    for attempt in range(max_attempts):
        status_response = requests.get(f"{BASE_URL}/{job_id}/status", headers=headers)
        status_response.raise_for_status()
        status_data = status_response.json()
        job_state = status_data.get("job_state")
        
        job_details = status_data.get("job_details", [{}])[0]
        pages = f"{job_details.get('pages_succeeded', 0)}/{job_details.get('total_pages', 0)}"
        print(f"  Attempt {attempt + 1}: {job_state} | Pages: {pages}")
        
        if job_state in ["Completed", "PartiallyCompleted"]:
            break
        elif job_state == "Failed":
            raise Exception(f"Job failed: {status_data.get('error_message')}")
        
        time.sleep(2)
    
    # Step 6: Download output
    print(f"Downloading output...")
    download_response = requests.post(f"{BASE_URL}/{job_id}/download-files", headers=headers)
    download_response.raise_for_status()
    download_data = download_response.json()
    
    output_files = []
    for fname, fdata in download_data.get("download_urls", {}).items():
        download_url = fdata["file_url"]
        file_response = requests.get(download_url)
        output_path = f"{file_path.stem}_output_{fname}"
        with open(output_path, "wb") as f:
            f.write(file_response.content)
        output_files.append(output_path)
        print(f"  ✓ Downloaded: {output_path}")
    
    # Step 7: Extract ZIP files
    extracted_dirs = []
    for output_file in output_files:
        if output_file.endswith('.zip'):
            extract_dir = output_file.replace('.zip', '_extracted')
            os.makedirs(extract_dir, exist_ok=True)
            with zipfile.ZipFile(output_file, 'r') as zip_ref:
                zip_ref.extractall(extract_dir)
            extracted_dirs.append(extract_dir)
            print(f"  ✓ Extracted to: {extract_dir}/")
    
    return {
        "job_id": job_id,
        "output_files": output_files,
        "extracted_dirs": extracted_dirs,
        "status": "completed"
    }


def main():
    """Example usage of Document Intelligence API."""
    
    print("=" * 60)
    print("Sarvam AI - Document Intelligence Examples")
    print("=" * 60)
    
    # Example 1: Process a PDF in Hindi
    print("\n" + "=" * 60)
    print("Example 1: Process Hindi PDF")
    print("=" * 60)
    
    try:
        result = process_document(
            "document.pdf",  # Replace with your PDF
            language="hi-IN",
            output_format="md"
        )
        print(f"\n✓ Processing complete!")
        print(f"  Job ID: {result['job_id']}")
        print(f"  Extracted to: {result['extracted_dirs'][0]}")
    except FileNotFoundError:
        print("  (Skipped - file not found)")
    
    # Example 2: Process with HTML output
    print("\n" + "=" * 60)
    print("Example 2: HTML Output Format")
    print("=" * 60)
    print("Use HTML for complex tables and structured documents")
    
    # Example 3: Process with JSON output
    print("\n" + "=" * 60)
    print("Example 3: JSON Output Format")
    print("=" * 60)
    print("Use JSON for programmatic processing and data extraction")
    
    # Example 4: Supported languages
    print("\n" + "=" * 60)
    print("Example 4: Supported Languages (23)")
    print("=" * 60)
    
    languages = [
        ("en-IN", "English"), ("hi-IN", "Hindi"), ("bn-IN", "Bengali"),
        ("ta-IN", "Tamil"), ("te-IN", "Telugu"), ("mr-IN", "Marathi"),
        ("gu-IN", "Gujarati"), ("kn-IN", "Kannada"), ("ml-IN", "Malayalam"),
        ("pa-IN", "Punjabi"), ("od-IN", "Odia")
    ]
    
    print("\nCore 11 + Extended 12 languages:")
    for code, name in languages:
        print(f"  • {name:<12} ({code})")
    print("  ... and 12 more")
    
    # Example 5: Use cases
    print("\n" + "=" * 60)
    print("Example 5: Use Case Scenarios")
    print("=" * 60)
    
    use_cases = [
        ("Financial Reports", "html", "Complex tables with merged cells"),
        ("Legal Documents", "md", "Preserves structure and reading order"),
        ("Academic Papers", "md", "Multi-column layouts, references"),
        ("Government Records", "html", "Forms and structured data"),
        ("Invoice Processing", "json", "Programmatic data extraction"),
    ]
    
    print("\nRecommended formats:")
    for name, fmt, desc in use_cases:
        print(f"  • {name:<20} ({fmt}): {desc}")


if __name__ == "__main__":
    main()
