# Sarvam AI Vision Skill Template

## Overview
This template helps you create skills that use Sarvam AI's Vision API for image analysis, captioning, OCR, and content extraction across 23 languages (22 Indian + English).

## API Information

**Model:** sarvam-vision (3B parameter Vision Language Model)  
**SDK:** `sarvamai` Python library  
**Client:** `client.vision`

## Capabilities

### 1. Image Captioning (`caption_in`)
Generate descriptive captions for images in Indian languages.

**Use Cases:**
- E-commerce product descriptions
- Social media content generation
- Accessibility (alt-text for visually impaired)
- Content moderation

### 2. OCR - Text Extraction (`default_ocr`)
Extract text from images containing documents, signs, screenshots.

**Use Cases:**
- Document digitization
- Receipt/invoice processing
- Sign board translation
- Screenshot text extraction

### 3. Markdown Extraction (`extract_as_markdown`)
Convert image content to structured markdown format.

**Use Cases:**
- Presentation slide conversion
- Form digitization
- Structured document processing
- Note-taking apps

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

## Python SDK Examples

### Example 1: Image Captioning (Hindi)

```python
import os
from sarvamai import SarvamAI

client = SarvamAI(api_subscription_key=os.getenv("SARVAM_API_KEY"))

# Generate caption in Hindi
with open("product_image.jpg", "rb") as image_file:
    response = client.vision.analyze(
        file=image_file,
        prompt_type="caption_in",
        language="hi-IN"
    )

print(response.content)  # "एक सुंदर लाल रंग की कार"
print(f"Request ID: {response.request_id}")
```

### Example 2: OCR - Text Extraction

```python
import os
from sarvamai import SarvamAI

client = SarvamAI(api_subscription_key=os.getenv("SARVAM_API_KEY"))

# Extract text from document image
with open("document.jpg", "rb") as image_file:
    response = client.vision.analyze(
        file=image_file,
        prompt_type="default_ocr"
    )

print(response.content)
print(f"Request ID: {response.request_id}")
```

### Example 3: Extract as Markdown

```python
import os
from sarvamai import SarvamAI

client = SarvamAI(api_subscription_key=os.getenv("SARVAM_API_KEY"))

# Convert image to markdown
with open("presentation_slide.jpg", "rb") as image_file:
    response = client.vision.analyze(
        file=image_file,
        prompt_type="extract_as_markdown"
    )

print(response.content)
print(f"Request ID: {response.request_id}")
```

## Prompt Types Reference

| Prompt Type | Description | Parameters | Output |
|-------------|-------------|------------|--------|
| `caption_in` | Image captioning in Indian languages | `file`, `prompt_type`, `language` | Descriptive caption in specified language |
| `default_ocr` | Text extraction (OCR) | `file`, `prompt_type` | Extracted text from image |
| `extract_as_markdown` | Convert to markdown | `file`, `prompt_type` | Markdown-formatted content |

## API Response Structure

The `analyze()` method returns an object with:

```python
{
    "content": "Generated caption or extracted text",
    "request_id": "unique_request_identifier"
}
```

**Attributes:**
- `content` (str): The generated caption, extracted text, or markdown content
- `request_id` (str): Unique identifier for the API request

## Use Case Examples

### 1. E-commerce Product Cataloging

**Challenge:** Generate product descriptions in multiple Indian languages  
**Solution:** Use `caption_in` with different language codes  
**Example:**

```python
from sarvamai import SarvamAI

client = SarvamAI(api_subscription_key="YOUR_API_KEY")

def generate_multilingual_descriptions(image_path):
    languages = ["hi-IN", "ta-IN", "te-IN", "mr-IN"]
    descriptions = {}
    
    for lang in languages:
        with open(image_path, "rb") as img:
            response = client.vision.analyze(
                file=img,
                prompt_type="caption_in",
                language=lang
            )
            descriptions[lang] = response.content
    
    return descriptions

# Usage
product_desc = generate_multilingual_descriptions("shoe.jpg")
print(product_desc["hi-IN"])  # Hindi description
print(product_desc["ta-IN"])  # Tamil description
```

### 2. Document Digitization

**Challenge:** Extract text from scanned documents  
**Solution:** Use `default_ocr` for text extraction  
**Example:**

```python
from sarvamai import SarvamAI

client = SarvamAI(api_subscription_key="YOUR_API_KEY")

def digitize_document(image_path):
    with open(image_path, "rb") as img:
        response = client.vision.analyze(
            file=img,
            prompt_type="default_ocr"
        )
    return response.content

# Extract text from scanned invoice
invoice_text = digitize_document("invoice_scan.jpg")
print(invoice_text)
```

### 3. Presentation to Markdown Converter

**Challenge:** Convert presentation slides to markdown notes  
**Solution:** Use `extract_as_markdown` for structured conversion  
**Example:**

```python
from sarvamai import SarvamAI
import os

client = SarvamAI(api_subscription_key="YOUR_API_KEY")

def convert_slides_to_markdown(slide_folder):
    markdown_notes = []
    
    for filename in sorted(os.listdir(slide_folder)):
        if filename.endswith(('.jpg', '.png')):
            filepath = os.path.join(slide_folder, filename)
            with open(filepath, "rb") as img:
                response = client.vision.analyze(
                    file=img,
                    prompt_type="extract_as_markdown"
                )
                markdown_notes.append(f"## Slide: {filename}\n\n{response.content}\n\n")
    
    return "\n".join(markdown_notes)

# Convert all slides to markdown
notes = convert_slides_to_markdown("./presentation_slides/")
with open("presentation_notes.md", "w") as f:
    f.write(notes)
```

### 4. Accessibility - Alt Text Generation

**Challenge:** Generate alt-text for images for screen readers  
**Solution:** Use `caption_in` with English or regional languages  
**Example:**

```python
from sarvamai import SarvamAI

client = SarvamAI(api_subscription_key="YOUR_API_KEY")

def generate_alt_text(image_path, language="en-IN"):
    with open(image_path, "rb") as img:
        response = client.vision.analyze(
            file=img,
            prompt_type="caption_in",
            language=language
        )
    return response.content

# Generate alt-text
alt_text = generate_alt_text("webpage_image.jpg", "hi-IN")
print(f'<img src="image.jpg" alt="{alt_text}">')
```

## Best Practices

### 1. Image Quality
- Use high-resolution images (recommended: 1024x1024 or higher)
- Ensure good lighting and clarity for OCR tasks
- Avoid blurry or low-quality images

### 2. File Format
- Supported formats: JPG, PNG
- Keep file sizes reasonable (< 10MB recommended)
- Use JPEG for photographs, PNG for documents/screenshots

### 3. Language Selection
- Always specify the correct language code for `caption_in`
- Use `en-IN` for English captions
- Language affects caption style and vocabulary

### 4. Prompt Type Selection
- **caption_in**: For descriptive understanding of images
- **default_ocr**: For text-heavy images (documents, signs)
- **extract_as_markdown**: For structured content (slides, forms)

### 5. Error Handling

```python
from sarvamai import SarvamAI
from sarvamai.core.api_error import ApiError

client = SarvamAI(api_subscription_key="YOUR_API_KEY")

def safe_vision_analyze(image_path, prompt_type, language=None):
    try:
        with open(image_path, "rb") as img:
            params = {"file": img, "prompt_type": prompt_type}
            if language:
                params["language"] = language
            
            response = client.vision.analyze(**params)
            return response.content
    
    except FileNotFoundError:
        print(f"Error: Image file '{image_path}' not found")
        return None
    except ApiError as e:
        print(f"API Error: {e.status_code} - {e.body}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Usage
result = safe_vision_analyze("image.jpg", "caption_in", "hi-IN")
if result:
    print(result)
```

## Prompt Type Comparison

| Feature | caption_in | default_ocr | extract_as_markdown |
|---------|-----------|-------------|---------------------|
| **Output** | Natural language description | Extracted text | Structured markdown |
| **Language Support** | 23 languages | Language-agnostic | Language-agnostic |
| **Best For** | Understanding image content | Text extraction | Structured conversion |
| **Use Cases** | Captioning, alt-text | OCR, digitization | Notes, documentation |
| **Parameters** | file, prompt_type, language | file, prompt_type | file, prompt_type |

## Complete Example with All Features

```python
import os
from sarvamai import SarvamAI

def analyze_image_all_modes(image_path):
    """Analyze image using all Vision API prompt types."""
    
    client = SarvamAI(api_subscription_key=os.getenv("SARVAM_API_KEY"))
    results = {}
    
    # 1. Caption in Hindi
    print("Generating Hindi caption...")
    with open(image_path, "rb") as img:
        response = client.vision.analyze(
            file=img,
            prompt_type="caption_in",
            language="hi-IN"
        )
        results["caption_hi"] = response.content
        print(f"  Hindi Caption: {response.content}")
    
    # 2. Caption in English
    print("\nGenerating English caption...")
    with open(image_path, "rb") as img:
        response = client.vision.analyze(
            file=img,
            prompt_type="caption_in",
            language="en-IN"
        )
        results["caption_en"] = response.content
        print(f"  English Caption: {response.content}")
    
    # 3. OCR extraction
    print("\nExtracting text (OCR)...")
    with open(image_path, "rb") as img:
        response = client.vision.analyze(
            file=img,
            prompt_type="default_ocr"
        )
        results["ocr"] = response.content
        print(f"  Extracted Text: {response.content}")
    
    # 4. Markdown extraction
    print("\nConverting to markdown...")
    with open(image_path, "rb") as img:
        response = client.vision.analyze(
            file=img,
            prompt_type="extract_as_markdown"
        )
        results["markdown"] = response.content
        print(f"  Markdown: {response.content}")
    
    return results

# Usage
if __name__ == "__main__":
    results = analyze_image_all_modes("sample_image.jpg")
    print("\n" + "="*60)
    print("Analysis Complete!")
    print("="*60)
```

## Resources

- [API Documentation](https://docs.sarvam.ai/api-reference-docs/vision)
- [Python SDK](https://pypi.org/project/sarvamai/)
- [Sarvam Vision Model](https://docs.sarvam.ai/api-reference-docs/getting-started/models/sarvam-vision)
- [Dashboard](https://dashboard.sarvam.ai)

## Common Issues and Solutions

### Issue 1: File not found error
**Solution:** Use absolute paths or verify file exists before opening

```python
import os
if os.path.exists(image_path):
    with open(image_path, "rb") as img:
        response = client.vision.analyze(...)
```

### Issue 2: Language not supported error
**Solution:** Verify language code is one of the 23 supported languages

### Issue 3: Large file size
**Solution:** Resize images before processing

```python
from PIL import Image

def resize_image(input_path, output_path, max_size=1024):
    img = Image.open(input_path)
    img.thumbnail((max_size, max_size))
    img.save(output_path)
```

## Next Steps

1. Get your API key from [Sarvam AI Dashboard](https://dashboard.sarvam.ai)
2. Install the SDK: `pip install sarvamai`
3. Try the examples above with your images
4. Explore different prompt types for your use case
5. Build your custom vision-based application
