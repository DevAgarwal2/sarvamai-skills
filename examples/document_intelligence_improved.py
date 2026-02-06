"""
Sarvam AI - Document Intelligence (IMPROVED)
--------------------------------------------
Enhanced version with better table and image handling.

Key improvements:
- Uses HTML format by default for better table preservation
- Shows extracted content structure
- Better error handling and diagnostics
- Displays metadata information

Model: sarvam-vision (3B parameter Vision Language Model)

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
import json
from pathlib import Path
from sarvamai import SarvamAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def process_document(
    file_path: str, 
    language: str = "en-IN", 
    output_format: str = "html",  # Changed default to HTML for better tables
    show_extracted_files: bool = True
):
    """
    Process a document using Sarvam AI Document Intelligence API.
    
    Args:
        file_path: Path to PDF or ZIP file
        language: Language code (default: en-IN)
        output_format: Output format - "html" (recommended) or "md" (default: html)
        show_extracted_files: Show what files were extracted (default: True)
    
    Returns:
        dict: Processing results including output file path
    """
    # Initialize client
    client = SarvamAI(api_subscription_key=os.getenv("SARVAM_API_KEY"))
    
    print(f"\n{'='*70}")
    print(f"Processing: {file_path}")
    print(f"Language: {language}")
    print(f"Output Format: {output_format.upper()}")
    print(f"{'='*70}")
    
    # Step 1: Create a document intelligence job
    print(f"\n[1/7] Creating job...")
    job = client.document_intelligence.create_job(
        language=language,
        output_format=output_format
    )
    print(f"  ✓ Job ID: {job.job_id}")
    
    # Step 2: Upload document
    print(f"\n[2/7] Uploading document...")
    job.upload_file(file_path)
    print(f"  ✓ File uploaded successfully")
    
    # Step 3: Start processing
    print(f"\n[3/7] Starting processing...")
    job.start()
    print(f"  ✓ Processing started")
    
    # Step 4: Wait for completion
    print(f"\n[4/7] Waiting for completion...")
    print(f"  (This may take a while depending on document size)")
    status = job.wait_until_complete()
    print(f"  ✓ Status: {status.job_state}")
    
    # Check for failures
    if status.job_state == "Failed":
        print(f"\n  ✗ ERROR: Job failed!")
        print(f"  Please check the document and try again.")
        return None
    
    # Step 5: Get processing metrics
    print(f"\n[5/7] Getting metrics...")
    metrics = job.get_page_metrics()
    print(f"  ✓ Pages processed: {metrics}")
    
    if metrics.get('pages_failed', 0) > 0:
        print(f"  ⚠ Warning: {metrics['pages_failed']} pages failed to process")
    
    # Step 6: Download output
    output_file = f"{os.path.splitext(file_path)[0]}_output.zip"
    print(f"\n[6/7] Downloading output...")
    job.download_output(output_file)
    print(f"  ✓ Downloaded: {output_file}")
    
    # Step 7: Extract and analyze
    extract_dir = f"{os.path.splitext(file_path)[0]}_extracted"
    print(f"\n[7/7] Extracting contents...")
    os.makedirs(extract_dir, exist_ok=True)
    
    with zipfile.ZipFile(output_file, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    
    print(f"  ✓ Extracted to: {extract_dir}/")
    
    # Show what was extracted
    if show_extracted_files:
        print(f"\n{'='*70}")
        print(f"EXTRACTED FILES:")
        print(f"{'='*70}")
        
        extracted_files = list(Path(extract_dir).rglob('*'))
        
        # Separate files by type
        html_files = [f for f in extracted_files if f.suffix == '.html']
        md_files = [f for f in extracted_files if f.suffix == '.md']
        json_files = [f for f in extracted_files if f.suffix == '.json']
        other_files = [f for f in extracted_files if f.is_file() and f.suffix not in ['.html', '.md', '.json']]
        
        if html_files:
            print(f"\n📄 HTML Files ({len(html_files)}):")
            for f in html_files:
                size = f.stat().st_size
                print(f"  • {f.name} ({size:,} bytes)")
                # Show first few lines
                try:
                    with open(f, 'r', encoding='utf-8') as file:
                        content = file.read(500)
                        if '<table' in content.lower():
                            print(f"    ✓ Contains tables")
                        if '<img' in content.lower():
                            print(f"    ✓ Contains images")
                except:
                    pass
        
        if md_files:
            print(f"\n📝 Markdown Files ({len(md_files)}):")
            for f in md_files:
                size = f.stat().st_size
                print(f"  • {f.name} ({size:,} bytes)")
                # Check for tables
                try:
                    with open(f, 'r', encoding='utf-8') as file:
                        content = file.read()
                        if '|' in content:
                            print(f"    ✓ Contains markdown tables")
                except:
                    pass
        
        if json_files:
            print(f"\n📋 Metadata Files ({len(json_files)}):")
            for f in json_files:
                print(f"  • {f.name}")
                # Show metadata summary
                try:
                    with open(f, 'r', encoding='utf-8') as file:
                        data = json.load(file)
                        if isinstance(data, dict):
                            if 'blocks' in data:
                                print(f"    ℹ Contains {len(data.get('blocks', []))} content blocks")
                            if 'tables' in data:
                                print(f"    ✓ Contains {len(data.get('tables', []))} tables")
                            if 'images' in data:
                                print(f"    ✓ Contains {len(data.get('images', []))} images")
                except:
                    pass
        
        if other_files:
            print(f"\n📎 Other Files ({len(other_files)}):")
            for f in other_files:
                print(f"  • {f.name} ({f.stat().st_size:,} bytes)")
        
        print(f"\n{'='*70}")
    
    # Final summary
    print(f"\n✓ PROCESSING COMPLETE!")
    print(f"{'='*70}")
    print(f"  Job ID: {job.job_id}")
    print(f"  Status: {status.job_state}")
    print(f"  Pages: {metrics.get('pages_processed', 'N/A')}/{metrics.get('total_pages', 'N/A')}")
    print(f"  Output: {extract_dir}/")
    print(f"{'='*70}\n")
    
    return {
        "job_id": job.job_id,
        "output_file": output_file,
        "extracted_dir": extract_dir,
        "status": status.job_state,
        "metrics": metrics,
        "extracted_files": {
            "html": [str(f) for f in html_files] if 'html_files' in locals() else [],
            "markdown": [str(f) for f in md_files] if 'md_files' in locals() else [],
            "metadata": [str(f) for f in json_files] if 'json_files' in locals() else []
        }
    }


def main():
    """Example usage with improved diagnostics."""
    
    print("\n" + "=" * 70)
    print("Sarvam AI - Document Intelligence (IMPROVED)")
    print("=" * 70)
    print("\nKey Features:")
    print("  • Better table extraction (uses HTML by default)")
    print("  • Shows extracted file structure")
    print("  • Displays metadata information")
    print("  • Better error handling")
    print("=" * 70)
    
    # Example 1: Process with HTML (best for tables)
    print("\n" + "=" * 70)
    print("Example 1: HTML Format (RECOMMENDED for tables)")
    print("=" * 70)
    print("\nHTML format preserves:")
    print("  ✓ Complex tables with merged cells")
    print("  ✓ Table formatting and structure")
    print("  ✓ Better layout preservation")
    print()
    
    try:
        result = process_document(
            "document.pdf",  # Replace with your PDF
            language="en-IN",
            output_format="html",  # Use HTML for tables
            show_extracted_files=True
        )
        
        if result:
            print(f"\n✓ Success! Check: {result['extracted_dir']}/")
    except FileNotFoundError:
        print("  (Skipped - document.pdf not found)")
        print("\n  To test:")
        print("    1. Place a PDF with tables/images in current directory")
        print("    2. Update the filename in the code")
        print("    3. Run again")
    except Exception as e:
        print(f"  ✗ Error: {e}")
        import traceback
        traceback.print_exc()
    
    # Example 2: Markdown format
    print("\n" + "=" * 70)
    print("Example 2: Markdown Format (for simple documents)")
    print("=" * 70)
    print("\nMarkdown format is good for:")
    print("  • Simple text documents")
    print("  • Documents without complex tables")
    print("  • When you need plain text output")
    print()
    print("Example:")
    print("""
    result = process_document(
        "simple_doc.pdf",
        language="hi-IN",
        output_format="md"
    )
    """)
    
    # Example 3: Recommendations
    print("\n" + "=" * 70)
    print("Example 3: Format Recommendations")
    print("=" * 70)
    print()
    print("📊 Documents with TABLES:")
    print("  → Use output_format='html'")
    print("  → HTML preserves table structure better")
    print()
    print("🖼  Documents with IMAGES:")
    print("  → Both formats work")
    print("  → Check metadata/ folder for coordinates")
    print()
    print("📄 Simple TEXT documents:")
    print("  → Use output_format='md'")
    print("  → Cleaner, more readable output")
    print()


if __name__ == "__main__":
    main()
