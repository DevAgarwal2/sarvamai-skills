"""
Sarvam AI - Document Intelligence with Batch Processing
-------------------------------------------------------
This example demonstrates how to process large PDFs by splitting them into
5-page chunks, processing each chunk separately, and merging the results.

This approach overcomes the 5-page limit by:
1. Splitting large PDFs into 5-page chunks
2. Processing each chunk via Document Intelligence API
3. Merging all outputs into a single HTML/MD file

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
import shutil
from pathlib import Path
from typing import List, Dict
from sarvamai import SarvamAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

try:
    from PyPDF2 import PdfReader, PdfWriter
except ImportError:
    print("ERROR: PyPDF2 is required. Install with: pip install PyPDF2")
    exit(1)


def split_pdf(input_pdf: str, pages_per_chunk: int = 5, output_dir: str = None) -> List[str]:
    """
    Split a PDF into smaller chunks of specified page size.
    
    Args:
        input_pdf: Path to input PDF file
        pages_per_chunk: Number of pages per chunk (default: 5)
        output_dir: Directory to save chunks (default: temp_chunks/)
    
    Returns:
        List of paths to chunk PDF files
    """
    if output_dir is None:
        output_dir = f"{os.path.splitext(input_pdf)[0]}_chunks"
    
    os.makedirs(output_dir, exist_ok=True)
    
    # Read the PDF
    reader = PdfReader(input_pdf)
    total_pages = len(reader.pages)
    
    print(f"\nSplitting PDF: {input_pdf}")
    print(f"  Total pages: {total_pages}")
    print(f"  Pages per chunk: {pages_per_chunk}")
    print(f"  Expected chunks: {(total_pages + pages_per_chunk - 1) // pages_per_chunk}")
    
    chunk_files = []
    
    # Split into chunks
    for chunk_num in range(0, total_pages, pages_per_chunk):
        writer = PdfWriter()
        
        # Add pages to this chunk
        end_page = min(chunk_num + pages_per_chunk, total_pages)
        for page_num in range(chunk_num, end_page):
            writer.add_page(reader.pages[page_num])
        
        # Save chunk
        chunk_filename = os.path.join(output_dir, f"chunk_{chunk_num//pages_per_chunk + 1:03d}.pdf")
        with open(chunk_filename, 'wb') as output_file:
            writer.write(output_file)
        
        chunk_files.append(chunk_filename)
        print(f"  ✓ Created chunk {len(chunk_files)}: pages {chunk_num + 1}-{end_page} → {chunk_filename}")
    
    return chunk_files


def process_chunk(client: SarvamAI, chunk_path: str, language: str, output_format: str) -> Dict:
    """
    Process a single PDF chunk using Document Intelligence API.
    
    Args:
        client: Initialized SarvamAI client
        chunk_path: Path to chunk PDF
        language: Language code (e.g., 'en-IN', 'hi-IN')
        output_format: Output format ('html' or 'md')
    
    Returns:
        Dictionary with job results and paths
    """
    chunk_name = os.path.basename(chunk_path)
    print(f"\n  Processing {chunk_name}...")
    
    # Create job
    job = client.document_intelligence.create_job(
        language=language,
        output_format=output_format
    )
    print(f"    ✓ Job created: {job.job_id}")
    
    # Upload file
    job.upload_file(chunk_path)
    print(f"    ✓ File uploaded")
    
    # Start processing
    job.start()
    print(f"    ✓ Job started")
    
    # Wait for completion
    status = job.wait_until_complete()
    print(f"    ✓ Completed: {status.job_state}")
    
    # Get metrics
    metrics = job.get_page_metrics()
    print(f"    ✓ Pages processed: {metrics}")
    
    # Download output
    output_zip = f"{os.path.splitext(chunk_path)[0]}_output.zip"
    job.download_output(output_zip)
    
    # Extract output
    extract_dir = f"{os.path.splitext(chunk_path)[0]}_extracted"
    os.makedirs(extract_dir, exist_ok=True)
    with zipfile.ZipFile(output_zip, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    print(f"    ✓ Extracted to {extract_dir}/")
    
    return {
        "chunk_path": chunk_path,
        "job_id": job.job_id,
        "output_zip": output_zip,
        "extract_dir": extract_dir,
        "status": status.job_state,
        "metrics": metrics
    }


def merge_markdown_outputs(chunk_results: List[Dict], output_file: str):
    """
    Merge all markdown outputs into a single file.
    
    Args:
        chunk_results: List of processing results from each chunk
        output_file: Path to merged output file
    """
    print(f"\nMerging Markdown outputs...")
    
    merged_content = []
    
    for i, result in enumerate(chunk_results, 1):
        extract_dir = result['extract_dir']
        
        # Find the markdown file in the extracted directory
        md_files = list(Path(extract_dir).glob("*.md"))
        
        if md_files:
            md_file = md_files[0]
            print(f"  ✓ Reading chunk {i}: {md_file}")
            
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                merged_content.append(f"<!-- Chunk {i} -->\n\n{content}")
        else:
            print(f"  ⚠ No markdown file found in {extract_dir}")
    
    # Write merged content
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n\n---\n\n'.join(merged_content))
    
    print(f"  ✓ Merged markdown saved to: {output_file}")


def merge_html_outputs(chunk_results: List[Dict], output_file: str):
    """
    Merge all HTML outputs into a single file while preserving original styling.
    
    Args:
        chunk_results: List of processing results from each chunk
        output_file: Path to merged output file
    """
    print(f"\nMerging HTML outputs...")
    
    # Extract CSS and content from first chunk to use as base
    first_chunk = chunk_results[0]
    extract_dir = first_chunk['extract_dir']
    html_files = list(Path(extract_dir).glob("*.html"))
    
    if not html_files:
        print(f"  ✗ No HTML files found")
        return
    
    # Read first chunk to get CSS
    with open(html_files[0], 'r', encoding='utf-8') as f:
        first_content = f.read()
    
    # Extract the CSS from first chunk
    css_start = first_content.find('<style>')
    css_end = first_content.find('</style>') + 8
    css_section = first_content[css_start:css_end] if css_start != -1 else ""
    
    # Start building merged HTML with original CSS
    html_parts = []
    html_parts.append("""<!DOCTYPE html>
<html lang="en-IN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Merged Document</title>
""")
    
    # Add original CSS styling
    html_parts.append(css_section)
    
    # Add minimal additional styling for page breaks
    html_parts.append("""    <style>
        .page-break {
            page-break-after: always;
            margin: 40px 0;
            border-bottom: 1px dashed #ccc;
        }
    </style>
</head>
<body>
""")
    
    # Merge all chunks
    for i, result in enumerate(chunk_results, 1):
        extract_dir = result['extract_dir']
        html_files = list(Path(extract_dir).glob("*.html"))
        
        if html_files:
            html_file = html_files[0]
            print(f"  ✓ Reading chunk {i}: {html_file}")
            
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Extract body content only (preserve all inner HTML)
                if '<body>' in content and '</body>' in content:
                    body_start = content.find('<body>') + 6
                    body_end = content.find('</body>')
                    content = content[body_start:body_end]
                
                # Add content directly without wrapping divs
                html_parts.append(content)
                
                # Add page break between chunks (except last one)
                if i < len(chunk_results):
                    html_parts.append('<div class="page-break"></div>')
        else:
            print(f"  ⚠ No HTML file found in {extract_dir}")
    
    html_parts.append("""
</body>
</html>
""")
    
    # Write merged HTML
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(html_parts))
    
    print(f"  ✓ Merged HTML saved to: {output_file}")


def process_pdf_directly(input_pdf: str, language: str, output_format: str) -> str:
    """
    Process a small PDF (≤5 pages) directly without splitting.
    
    Args:
        input_pdf: Path to input PDF file
        language: Language code
        output_format: Output format ('html' or 'md')
    
    Returns:
        Path to output file
    """
    print("\nProcessing PDF directly (no chunking)...")
    
    # Initialize client
    client = SarvamAI(api_subscription_key=os.getenv("SARVAM_API_KEY"))
    
    # Create job
    print(f"  Creating job...")
    job = client.document_intelligence.create_job(
        language=language,
        output_format=output_format
    )
    print(f"  ✓ Job created: {job.job_id}")
    
    # Upload file
    print("  Uploading file...")
    job.upload_file(input_pdf)
    print("  ✓ File uploaded")
    
    # Start processing
    print("  Starting processing...")
    job.start()
    print("  ✓ Job started")
    
    # Wait for completion
    print("  Waiting for completion...")
    status = job.wait_until_complete()
    print(f"  ✓ Completed: {status.job_state}")
    
    # Get metrics
    metrics = job.get_page_metrics()
    print(f"  ✓ Pages processed: {metrics}")
    
    # Download output
    output_zip = f"{os.path.splitext(input_pdf)[0]}_output.zip"
    print(f"  Downloading output...")
    job.download_output(output_zip)
    print(f"  ✓ Output saved to {output_zip}")
    
    # Extract output
    extract_dir = f"{os.path.splitext(input_pdf)[0]}_extracted"
    os.makedirs(extract_dir, exist_ok=True)
    with zipfile.ZipFile(output_zip, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    print(f"  ✓ Extracted to {extract_dir}/")
    
    # Find the output file
    output_files = list(Path(extract_dir).glob(f"*.{output_format}"))
    if output_files:
        # Copy to final location
        final_output = f"{os.path.splitext(input_pdf)[0]}_output.{output_format}"
        shutil.copy(output_files[0], final_output)
        
        # Cleanup
        shutil.rmtree(extract_dir)
        os.remove(output_zip)
        
        print(f"\n{'=' * 70}")
        print(f"✓ Processing Complete!")
        print("=" * 70)
        print(f"  Input PDF: {input_pdf}")
        print(f"  Output format: {output_format}")
        print(f"  Output file: {final_output}")
        print("=" * 70)
        
        return final_output
    else:
        raise FileNotFoundError(f"No output file found in {extract_dir}")


def cleanup_temporary_files(chunks_dir: str, chunk_results: List[Dict], keep_chunks: bool = False):
    """
    Clean up temporary files created during processing.
    
    Args:
        chunks_dir: Directory containing chunk PDFs
        chunk_results: List of processing results
        keep_chunks: If True, keep the chunk PDFs (default: False)
    """
    print(f"\nCleaning up temporary files...")
    
    # Clean up extracted directories and zip files
    for result in chunk_results:
        # Remove extracted directory
        if os.path.exists(result['extract_dir']):
            shutil.rmtree(result['extract_dir'])
            print(f"  ✓ Removed {result['extract_dir']}")
        
        # Remove zip file
        if os.path.exists(result['output_zip']):
            os.remove(result['output_zip'])
            print(f"  ✓ Removed {result['output_zip']}")
    
    # Remove chunks directory if requested
    if not keep_chunks and os.path.exists(chunks_dir):
        shutil.rmtree(chunks_dir)
        print(f"  ✓ Removed chunks directory: {chunks_dir}")


def process_large_pdf(
    input_pdf: str,
    language: str = "en-IN",
    output_format: str = "html",  # Changed default to HTML for better table preservation
    pages_per_chunk: int = 5,
    cleanup: bool = True,
    keep_chunks: bool = False
) -> str:
    """
    Process a large PDF by splitting into chunks and merging results.
    
    Intelligently handles PDFs of any size:
    - PDFs with ≤5 pages: Processes directly without splitting
    - PDFs with >5 pages: Splits into chunks and merges results
    
    Args:
        input_pdf: Path to input PDF file
        language: Language code (default: 'en-IN')
        output_format: Output format - 'html' (recommended) or 'md' (default: 'html')
        pages_per_chunk: Number of pages per chunk (default: 5)
        cleanup: Whether to clean up temporary files (default: True)
        keep_chunks: Whether to keep chunk PDFs after processing (default: False)
    
    Returns:
        Path to merged output file
    """
    print("=" * 70)
    print(f"Processing PDF with Batch Document Intelligence")
    print("=" * 70)
    
    # Check PDF page count first
    from PyPDF2 import PdfReader
    reader = PdfReader(input_pdf)
    total_pages = len(reader.pages)
    
    print(f"\nPDF Analysis:")
    print(f"  File: {input_pdf}")
    print(f"  Total pages: {total_pages}")
    
    # If PDF has 5 or fewer pages, process directly without splitting
    if total_pages <= pages_per_chunk:
        print(f"  Strategy: Direct processing (no splitting needed)")
        print("=" * 70)
        return process_pdf_directly(input_pdf, language, output_format)
    
    # For larger PDFs, use batch processing
    print(f"  Strategy: Batch processing with {pages_per_chunk}-page chunks")
    print("=" * 70)
    
    # Initialize client
    client = SarvamAI(api_subscription_key=os.getenv("SARVAM_API_KEY"))
    
    # Step 1: Split PDF into chunks
    chunks_dir = f"{os.path.splitext(input_pdf)[0]}_chunks"
    chunk_files = split_pdf(input_pdf, pages_per_chunk=pages_per_chunk, output_dir=chunks_dir)
    
    # Step 2: Process each chunk
    print(f"\n{'=' * 70}")
    print(f"Processing {len(chunk_files)} chunks...")
    print("=" * 70)
    
    chunk_results = []
    for chunk_file in chunk_files:
        try:
            result = process_chunk(client, chunk_file, language, output_format)
            chunk_results.append(result)
        except Exception as e:
            print(f"  ✗ Error processing {chunk_file}: {e}")
    
    # Step 3: Merge outputs
    print(f"\n{'=' * 70}")
    print(f"Merging outputs...")
    print("=" * 70)
    
    output_file = f"{os.path.splitext(input_pdf)[0]}_merged.{output_format}"
    
    if output_format == "md":
        merge_markdown_outputs(chunk_results, output_file)
    elif output_format == "html":
        merge_html_outputs(chunk_results, output_file)
    
    # Step 4: Cleanup
    if cleanup:
        cleanup_temporary_files(chunks_dir, chunk_results, keep_chunks=keep_chunks)
    
    # Final summary
    print(f"\n{'=' * 70}")
    print(f"✓ Processing Complete!")
    print("=" * 70)
    print(f"  Input PDF: {input_pdf}")
    print(f"  Total chunks processed: {len(chunk_results)}")
    print(f"  Output format: {output_format}")
    print(f"  Merged output: {output_file}")
    print("=" * 70)
    
    return output_file


def main():
    """Example usage of batch document intelligence processing."""
    
    print("\n" + "=" * 70)
    print("Sarvam AI - Batch Document Intelligence Examples")
    print("=" * 70)
    
    # Example 1: Small PDF (≤5 pages) - Direct processing
    print("\n" + "=" * 70)
    print("Example 1: Small PDF (≤5 pages) → Direct Processing")
    print("=" * 70)
    print("PDFs with 5 or fewer pages are processed directly without splitting")
    print()
    print("Example usage:")
    print("""
    output = process_large_pdf(
        input_pdf="small_doc.pdf",     # 3 pages
        language="en-IN",
        output_format="html"  # HTML recommended for tables
    )
    # Output: small_doc_output.html (processed directly)
    """)
    
    # Example 2: Medium PDF (10-15 pages) - Batch processing
    print("\n" + "=" * 70)
    print("Example 2: Medium PDF (10-15 pages) → Batch Processing")
    print("=" * 70)
    print("A 10-page PDF will be split into 2 chunks of 5 pages each")
    print()
    
    try:
        output_file = process_large_pdf(
            input_pdf="medium_document.pdf",  # Replace with your PDF
            language="en-IN",
            output_format="html",  # HTML for better table/image handling
            pages_per_chunk=5,
            cleanup=True,
            keep_chunks=False
        )
        print(f"\n✓ Success! Output saved to: {output_file}")
    except FileNotFoundError:
        print("  (Skipped - medium_document.pdf not found)")
        print("\n  For a 10-page PDF:")
        print("    → Split into 2 chunks (5+5 pages)")
        print("    → Process each chunk via API")
        print("    → Merge into medium_document_merged.md")
    except Exception as e:
        print(f"  Error: {e}")
    
    # Example 3: Large PDF (25+ pages) - Batch processing
    print("\n" + "=" * 70)
    print("Example 3: Large PDF (25 pages) → Batch Processing")
    print("=" * 70)
    print("A 25-page PDF will be split into 5 chunks of 5 pages each")
    print()
    print("Example usage:")
    print("""
    output = process_large_pdf(
        input_pdf="large_document.pdf",  # 25 pages
        language="hi-IN",
        output_format="html",
        pages_per_chunk=5
    )
    # → 5 chunks: 5+5+5+5+5 pages
    # → Output: large_document_merged.html
    """)
    
    # Example 4: Size-based strategy summary
    print("\n" + "=" * 70)
    print("Example 4: Automatic Strategy Selection")
    print("=" * 70)
    print("The function automatically chooses the best strategy:\n")
    print("  📄 ≤5 pages:   Direct processing (no splitting)")
    print("  📚 6-10 pages: Split into 2 chunks")
    print("  📖 11-15 pages: Split into 3 chunks")
    print("  📕 16-20 pages: Split into 4 chunks")
    print("  📗 21-25 pages: Split into 5 chunks")
    print("  📘 26+ pages:  Split into 6+ chunks")
    print()
    print("All chunks are automatically merged in correct order!")
    
    # Example 5: HTML vs Markdown for different sizes
    print("\n" + "=" * 70)
    print("Example 5: Format Recommendations by Size")
    print("=" * 70)
    print()
    print("Small PDFs (≤5 pages):")
    print("  • Markdown: Simple documents, articles, reports")
    print("  • HTML: Forms, tables, structured data")
    print()
    print("Large PDFs (25+ pages):")
    print("  • Markdown: Books, research papers, long reports")
    print("  • HTML: Financial reports, invoices, complex tables")
    
    # Example 6: Custom chunk size
    print("\n" + "=" * 70)
    print("Example 6: Custom Chunk Size")
    print("=" * 70)
    print("Adjust chunk size based on your needs:")
    print()
    print("Smaller chunks (3 pages):")
    print("""
    output = process_large_pdf(
        input_pdf="document.pdf",
        pages_per_chunk=3  # More API calls but faster per chunk
    )
    """)
    print()
    print("Larger chunks (5 pages - recommended):")
    print("""
    output = process_large_pdf(
        input_pdf="document.pdf",
        pages_per_chunk=5  # Fewer API calls, optimal size
    )
    """)


if __name__ == "__main__":
    main()
