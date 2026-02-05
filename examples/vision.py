"""
Sarvam AI Vision API Examples

The Vision API provides image analysis capabilities using the sarvam-vision model.
Supports multiple prompt types for different use cases.

Model: sarvam-vision (3B parameter Vision Language Model)

Supported Prompt Types:
- caption_in: Generate captions in Indian languages (with language parameter)
- default_ocr: Extract text from images (OCR)
- extract_as_markdown: Convert image content to markdown format

Supported Languages (for caption_in): 23 languages (22 Indian + English)

NOTE: Vision API is currently accessed via REST API. SDK support coming soon.
"""

import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
VISION_API_URL = "https://api.sarvam.ai/vision"


def analyze_image_caption(file_path: str, language: str = "hi-IN"):
    """
    Generate image captions in Indian languages.
    
    Args:
        file_path: Path to image file (JPG, PNG)
        language: Language code for caption (default: hi-IN)
                  Supported: hi-IN, en-IN, bn-IN, gu-IN, kn-IN, ml-IN, mr-IN, 
                            od-IN, pa-IN, ta-IN, te-IN, as-IN, ur-IN, sa-IN, 
                            ne-IN, doi-IN, brx-IN, kok-IN, mai-IN, sd-IN, ks-IN, 
                            mni-IN, sat-IN
    
    Returns:
        dict: Caption content and request ID
    """
    print(f"\n{'='*60}")
    print(f"Generating Caption in {language}")
    print(f"{'='*60}")
    print(f"Image: {file_path}")
    print(f"Prompt Type: caption_in")
    
    headers = {
        "API-Subscription-Key": os.getenv("SARVAM_API_KEY")
    }
    
    files = {
        "file": (os.path.basename(file_path), open(file_path, "rb"), "image/jpeg")
    }
    
    data = {
        "prompt_type": "caption_in",
        "language": language
    }
    
    response = requests.post(VISION_API_URL, headers=headers, files=files, data=data)
    response.raise_for_status()
    
    result = response.json()
    
    print(f"\nCaption ({language}):")
    print(f"  {result['content']}")
    print(f"\nRequest ID: {result['request_id']}")
    
    return result


def analyze_image_ocr(file_path: str):
    """
    Extract text from images using OCR.
    
    Args:
        file_path: Path to image file (JPG, PNG)
    
    Returns:
        dict: Extracted text and request ID
    """
    print(f"\n{'='*60}")
    print(f"Extracting Text (OCR)")
    print(f"{'='*60}")
    print(f"Image: {file_path}")
    print(f"Prompt Type: default_ocr")
    
    headers = {
        "API-Subscription-Key": os.getenv("SARVAM_API_KEY")
    }
    
    files = {
        "file": (os.path.basename(file_path), open(file_path, "rb"), "image/jpeg")
    }
    
    data = {
        "prompt_type": "default_ocr"
    }
    
    response = requests.post(VISION_API_URL, headers=headers, files=files, data=data)
    response.raise_for_status()
    
    result = response.json()
    
    print(f"\nExtracted Text:")
    print(f"  {result['content']}")
    print(f"\nRequest ID: {result['request_id']}")
    
    return result


def analyze_image_markdown(file_path: str):
    """
    Convert image content to markdown format.
    
    Args:
        file_path: Path to image file (JPG, PNG)
    
    Returns:
        dict: Markdown content and request ID
    """
    print(f"\n{'='*60}")
    print(f"Extracting as Markdown")
    print(f"{'='*60}")
    print(f"Image: {file_path}")
    print(f"Prompt Type: extract_as_markdown")
    
    headers = {
        "API-Subscription-Key": os.getenv("SARVAM_API_KEY")
    }
    
    files = {
        "file": (os.path.basename(file_path), open(file_path, "rb"), "image/jpeg")
    }
    
    data = {
        "prompt_type": "extract_as_markdown"
    }
    
    response = requests.post(VISION_API_URL, headers=headers, files=files, data=data)
    response.raise_for_status()
    
    result = response.json()
    
    print(f"\nMarkdown Content:")
    print(f"  {result['content']}")
    print(f"\nRequest ID: {result['request_id']}")
    
    return result


def main():
    """Demonstrate all Vision API capabilities."""
    
    print("\n" + "="*60)
    print("Sarvam AI Vision API - Complete Examples")
    print("="*60)
    
    # Example 1: Image Captioning in Hindi
    print("\n" + "="*60)
    print("Example 1: Image Captioning (Hindi)")
    print("="*60)
    print("Generate descriptive captions for images in Indian languages")
    print("\nUsage:")
    print("  result = analyze_image_caption('image.jpg', 'hi-IN')")
    print("\nExample:")
    try:
        # Replace with your image path
        result = analyze_image_caption("sample_image.jpg", "hi-IN")
        print(f"\n✓ Caption generated successfully!")
    except FileNotFoundError:
        print("  (Skipped - sample image not found)")
        print("\n  To test, run:")
        print("    analyze_image_caption('your_image.jpg', 'hi-IN')")
    except Exception as e:
        print(f"  Error: {e}")
    
    # Example 2: OCR - Text Extraction
    print("\n" + "="*60)
    print("Example 2: OCR - Text Extraction")
    print("="*60)
    print("Extract text from images containing documents, signs, etc.")
    print("\nUsage:")
    print("  result = analyze_image_ocr('document.jpg')")
    print("\nBest for: Documents, screenshots, text-heavy images")
    
    # Example 3: Markdown Extraction
    print("\n" + "="*60)
    print("Example 3: Extract as Markdown")
    print("="*60)
    print("Convert image content to structured markdown format")
    print("\nUsage:")
    print("  result = analyze_image_markdown('slide.jpg')")
    print("\nBest for: Presentations, structured documents, forms")
    
    # Example 4: Multi-language Captioning
    print("\n" + "="*60)
    print("Example 4: Multi-language Captioning")
    print("="*60)
    print("Generate captions in different Indian languages:")
    print("\nSupported Languages (23):")
    languages = [
        ("Hindi", "hi-IN"), ("English", "en-IN"), ("Bengali", "bn-IN"),
        ("Tamil", "ta-IN"), ("Telugu", "te-IN"), ("Marathi", "mr-IN"),
        ("Gujarati", "gu-IN"), ("Kannada", "kn-IN"), ("Malayalam", "ml-IN"),
        ("Punjabi", "pa-IN"), ("Odia", "od-IN"), ("Assamese", "as-IN"),
        ("Urdu", "ur-IN"), ("Sanskrit", "sa-IN"), ("Nepali", "ne-IN"),
        ("Dogri", "doi-IN"), ("Bodo", "brx-IN"), ("Konkani", "kok-IN"),
        ("Maithili", "mai-IN"), ("Sindhi", "sd-IN"), ("Kashmiri", "ks-IN"),
        ("Manipuri", "mni-IN"), ("Santali", "sat-IN")
    ]
    
    for i in range(0, len(languages), 3):
        batch = languages[i:i+3]
        print(f"  {' | '.join([f'{lang}: {code}' for lang, code in batch])}")
    
    # Example 5: Use Cases
    print("\n" + "="*60)
    print("Example 5: Common Use Cases")
    print("="*60)
    
    use_cases = [
        ("E-commerce", "caption_in", "Product image descriptions in regional languages"),
        ("Education", "extract_as_markdown", "Convert slides/notes to markdown"),
        ("Document Digitization", "default_ocr", "Extract text from scanned documents"),
        ("Accessibility", "caption_in", "Generate image descriptions for visually impaired"),
        ("Content Moderation", "caption_in", "Understand image content in Indian languages"),
    ]
    
    print("\nRecommended prompt types:")
    for use_case, prompt_type, description in use_cases:
        print(f"\n  • {use_case}")
        print(f"    Prompt: {prompt_type}")
        print(f"    Use: {description}")
    
    # Example 6: API Response Structure
    print("\n" + "="*60)
    print("Example 6: API Response Structure")
    print("="*60)
    print("\nThe API returns JSON with:")
    print("  • content: The generated caption/extracted text")
    print("  • request_id: Unique identifier for the request")
    print("  • prompt: The prompt used by the API")
    print("\nExample response:")
    print("  {")
    print("    'content': 'एक सुंदर पहाड़ी दृश्य',")
    print("    'request_id': 'vision_123456789',")
    print("    'prompt': 'Describe this image in Hindi.'")
    print("  }")


if __name__ == "__main__":
    main()
