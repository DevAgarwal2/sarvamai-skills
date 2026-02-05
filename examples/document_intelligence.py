"""
Sarvam AI - Document Intelligence
----------------------------------
This example demonstrates how to use Sarvam AI's Document Intelligence API
to extract text from PDFs and images in 23 languages (22 Indian + English).

Model: sarvam-vision (3B parameter Vision Language Model)

Supported Input Formats: PDF, ZIP (containing JPG/PNG images)
Output Formats (delivered as ZIP): html, md (json is NOT supported)

Supported languages (23): hi-IN, en-IN, bn-IN, gu-IN, kn-IN, ml-IN, mr-IN, od-IN, pa-IN, ta-IN, te-IN,
                          as-IN, ur-IN, sa-IN, ne-IN, doi-IN, brx-IN, kok-IN, mai-IN, sd-IN, ks-IN, mni-IN, sat-IN
"""

import os
import zipfile
from sarvamai import SarvamAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def process_document(file_path: str, language: str = "en-IN", output_format: str = "md"):
    """
    Process a document using Sarvam AI Document Intelligence API.
    
    Args:
        file_path: Path to PDF or ZIP file
        language: Language code (default: en-IN)
        output_format: Output format - "html" or "md" only (default: md)
    
    Returns:
        dict: Processing results including output file path
    """
    # Initialize client
    client = SarvamAI(api_subscription_key=os.getenv("SARVAM_API_KEY"))
    
    # Step 1: Create a document intelligence job
    print(f"Creating job for {file_path}...")
    job = client.document_intelligence.create_job(
        language=language,
        output_format=output_format
    )
    print(f"  ✓ Job created: {job.job_id}")
    
    # Step 2: Upload document
    print("Uploading document...")
    job.upload_file(file_path)
    print("  ✓ File uploaded")
    
    # Step 3: Start processing
    print("Starting processing...")
    job.start()
    print("  ✓ Job started")
    
    # Step 4: Wait for completion (with timeout)
    print("Waiting for completion...")
    status = job.wait_until_complete()
    print(f"  ✓ Job completed with state: {status.job_state}")
    
    # Step 5: Get processing metrics
    metrics = job.get_page_metrics()
    print(f"  ✓ Pages processed: {metrics}")
    
    # Step 6: Download output (ZIP file containing the processed document)
    output_file = f"{os.path.splitext(file_path)[0]}_output.zip"
    print(f"Downloading output to {output_file}...")
    job.download_output(output_file)
    print(f"  ✓ Output saved to {output_file}")
    
    # Step 7: Auto-extract ZIP file
    extract_dir = f"{os.path.splitext(file_path)[0]}_extracted"
    print(f"Extracting to {extract_dir}/...")
    os.makedirs(extract_dir, exist_ok=True)
    with zipfile.ZipFile(output_file, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    print(f"  ✓ Extracted to {extract_dir}/")
    
    return {
        "job_id": job.job_id,
        "output_file": output_file,
        "extracted_dir": extract_dir,
        "status": status.job_state,
        "metrics": metrics
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
        print(f"  Output ZIP: {result['output_file']}")
        print(f"  Extracted to: {result['extracted_dir']}")
    except FileNotFoundError:
        print("  (Skipped - file not found)")
    except Exception as e:
        print(f"  Error: {e}")
    
    # Example 2: Process with HTML output
    print("\n" + "=" * 60)
    print("Example 2: HTML Output Format")
    print("=" * 60)
    print("Use HTML for complex tables and structured documents")
    print("\nExample:")
    print("  result = process_document('document.pdf', 'en-IN', 'html')")
    
    # Example 3: Supported formats
    print("\n" + "=" * 60)
    print("Example 3: Supported Output Formats")
    print("=" * 60)
    print("✅ Supported: 'html', 'md'")
    print("❌ NOT supported: 'json' (will cause API error)")
    
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
        ("Invoice Processing", "html", "Extract structured table data"),
    ]
    
    print("\nRecommended formats:")
    for name, fmt, desc in use_cases:
        print(f"  • {name:<20} ({fmt}): {desc}")


if __name__ == "__main__":
    main()
