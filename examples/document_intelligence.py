"""
Sarvam AI - Document Intelligence
----------------------------------
This example demonstrates how to use Sarvam AI's Document Intelligence API
to extract text from PDFs and images in 23 languages (22 Indian + English).

Model: sarvam-vision (3B parameter Vision Language Model)

Supported Input Formats: PDF, ZIP (containing JPG/PNG images)
Output Formats (delivered as ZIP): html, md (json is NOT supported)

Supported Languages (23):
  Core 11: hi-IN (Hindi/Devanagari), en-IN (English/Latin), bn-IN (Bengali), 
           gu-IN (Gujarati), kn-IN (Kannada), ml-IN (Malayalam), mr-IN (Marathi/Devanagari),
           od-IN (Odia), pa-IN (Punjabi/Gurmukhi), ta-IN (Tamil), te-IN (Telugu)
  
  Extended 12: as-IN (Assamese), ur-IN (Urdu/Perso-Arabic), sa-IN (Sanskrit/Devanagari),
               ne-IN (Nepali/Devanagari), kok-IN (Konkani/Devanagari), mai-IN (Maithili/Devanagari),
               sd-IN (Sindhi/Devanagari-Arabic), ks-IN (Kashmiri/Perso-Arabic),
               doi-IN (Dogri/Devanagari), mni-IN (Manipuri/Meetei Mayek),
               brx-IN (Bodo/Devanagari), sat-IN (Santali/Ol Chiki)
"""

import os
import zipfile
from sarvamai import SarvamAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def process_document(file_path: str, language: str = "en-IN", output_format: str = "html"):
    """
    Process a document using Sarvam AI Document Intelligence API.
    
    Args:
        file_path: Path to PDF or ZIP file
        language: Language code (default: en-IN)
        output_format: Output format - "html" (recommended for tables) or "md" (default: html)
    
    Returns:
        dict: Processing results including output file path
    
    Note: Use 'html' format for documents with tables/complex layouts
          Use 'md' format for simple text documents
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
    
    # Check for failures
    if status.job_state == "Failed":
        print(f"\n  ✗ ERROR: Processing failed!")
        return None
    
    # Step 5: Get processing metrics
    metrics = job.get_page_metrics()
    print(f"  ✓ Pages processed: {metrics}")
    
    if metrics.get('pages_failed', 0) > 0:
        print(f"  ⚠ Warning: {metrics['pages_failed']} pages failed")
    
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
    
    # Show extracted files
    from pathlib import Path
    extracted_files = list(Path(extract_dir).rglob('*'))
    html_files = [f for f in extracted_files if f.suffix == '.html']
    md_files = [f for f in extracted_files if f.suffix == '.md']
    
    print(f"\n  Extracted files:")
    if html_files:
        for f in html_files:
            print(f"    • {f.name} ({f.stat().st_size:,} bytes)")
    if md_files:
        for f in md_files:
            print(f"    • {f.name} ({f.stat().st_size:,} bytes)")
    
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
    
    # Example 1: Process a PDF with tables (use HTML)
    print("\n" + "=" * 60)
    print("Example 1: Process PDF with Tables → HTML Format")
    print("=" * 60)
    print("Use HTML format for documents with tables/complex layouts")
    print()
    
    try:
        result = process_document(
            "document.pdf",  # Replace with your PDF
            language="hi-IN",
            output_format="html"  # HTML for better table preservation
        )
        if result:
            print(f"\n✓ Processing complete!")
            print(f"  Job ID: {result['job_id']}")
            print(f"  Output ZIP: {result['output_file']}")
            print(f"  Extracted to: {result['extracted_dir']}")
    except FileNotFoundError:
        print("  (Skipped - file not found)")
    except Exception as e:
        print(f"  Error: {e}")
    
    # Example 2: Simple text document with Markdown
    print("\n" + "=" * 60)
    print("Example 2: Simple Text Document → Markdown Format")
    print("=" * 60)
    print("Use Markdown for simple text documents without complex tables")
    print("\nExample:")
    print("  result = process_document('simple_doc.pdf', 'en-IN', 'md')")
    
    # Example 3: Format recommendations
    print("\n" + "=" * 60)
    print("Example 3: Format Recommendations")
    print("=" * 60)
    print()
    print("📊 Documents with TABLES:")
    print("  → Use output_format='html'")
    print("  → Better preservation of table structure")
    print()
    print("🖼  Documents with IMAGES:")
    print("  → Both formats work")
    print("  → Check metadata/ folder for details")
    print()
    print("📄 Simple TEXT documents:")
    print("  → Use output_format='md'")
    print("  → Cleaner, more readable")
    print()
    print("✅ Supported formats: 'html', 'md'")
    print("❌ NOT supported: 'json'")
    
    # Example 4: Supported languages
    print("\n" + "=" * 60)
    print("Example 4: Supported Languages (23)")
    print("=" * 60)
    
    print("\nCore 11 Languages:")
    core_languages = [
        ("en-IN", "English", "Latin"),
        ("hi-IN", "Hindi", "Devanagari"),
        ("bn-IN", "Bengali", "Bengali"),
        ("ta-IN", "Tamil", "Tamil"),
        ("te-IN", "Telugu", "Telugu"),
        ("mr-IN", "Marathi", "Devanagari"),
        ("gu-IN", "Gujarati", "Gujarati"),
        ("kn-IN", "Kannada", "Kannada"),
        ("ml-IN", "Malayalam", "Malayalam"),
        ("pa-IN", "Punjabi", "Gurmukhi"),
        ("od-IN", "Odia", "Odia")
    ]
    
    for code, name, script in core_languages:
        print(f"  • {name:<12} ({code:<8}) - {script}")
    
    print("\nExtended 12 Languages:")
    extended_languages = [
        ("as-IN", "Assamese", "Assamese"),
        ("ur-IN", "Urdu", "Perso-Arabic"),
        ("sa-IN", "Sanskrit", "Devanagari"),
        ("ne-IN", "Nepali", "Devanagari"),
        ("kok-IN", "Konkani", "Devanagari"),
        ("mai-IN", "Maithili", "Devanagari"),
        ("sd-IN", "Sindhi", "Devanagari/Arabic"),
        ("ks-IN", "Kashmiri", "Perso-Arabic"),
        ("doi-IN", "Dogri", "Devanagari"),
        ("mni-IN", "Manipuri", "Meetei Mayek"),
        ("brx-IN", "Bodo", "Devanagari"),
        ("sat-IN", "Santali", "Ol Chiki")
    ]
    
    for code, name, script in extended_languages:
        print(f"  • {name:<12} ({code:<8}) - {script}")
    
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
