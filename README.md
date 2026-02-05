# Sarvam AI Skills

A comprehensive collection of templates, examples, and resources for building AI-powered applications using Sarvam AI APIs. This repository provides everything you need to integrate Indian language AI capabilities into your applications.

## Overview

Sarvam AI provides state-of-the-art AI models for Indian languages, including:
- **Speech-to-Text**: Transcribe audio in 11+ Indian languages
- **Text-to-Speech**: Generate natural-sounding speech
- **Translation**: Translate between Indian languages and English
- **Chat Completion**: Conversational AI and text generation
- **Document Intelligence**: Extract text from PDFs and images in 23 languages
- **Vision**: Image captioning, OCR, and content extraction in 23 languages

This repository helps you quickly build applications using these capabilities.

## Quick Start

### Prerequisites

1. **Get an API Key**
   - Visit [Sarvam AI Dashboard](https://dashboard.sarvam.ai)
   - Create an account and generate an API key

2. **Install the SDK**
   ```bash
   pip install sarvamai
   ```

3. **Set Up Environment**
   ```bash
   # Copy the example env file
   cp .env.example .env
   
   # Add your API key to .env
   echo "SARVAM_API_KEY=your_api_key_here" > .env
   ```

### Your First Request

```python
from sarvamai import SarvamAI
import os

# Initialize client
client = SarvamAI(api_subscription_key=os.getenv("SARVAM_API_KEY"))

# Translate text
response = client.text.translate(
    input="Hello, how are you?",
    source_language_code="en-IN",
    target_language_code="hi-IN"
)

print(response.translated_text)
# Output: नमस्ते, आप कैसे हैं?
```

## Repository Structure

```
sarvam-skills/
├── examples/           # Working code examples for all APIs
│   ├── speech_to_text.py
│   ├── speech_to_text_translate.py
│   ├── text_to_speech.py
│   ├── text_translation.py
│   ├── chat_completion.py
│   ├── document_intelligence.py
│   ├── end_to_end_example.py
│   └── README.md
│
├── templates/          # Comprehensive skill templates and guides
│   ├── speech-to-text-template.md
│   ├── text-to-speech-template.md
│   ├── text-translation-template.md
│   ├── chat-completion-template.md
│   ├── document-intelligence-template.md
│   ├── skill-template.md
│   └── README.md
│
├── .env.example       # Example environment configuration
└── README.md          # This file
```

## Available APIs

### 1. Speech to Text
Convert audio to text in Indian languages.

```python
response = client.speech_to_text.transcribe(
    file=open("audio.wav", "rb"),
    
    language_code="hi-IN"
)
```

**Use Cases:** Voice notes, meeting transcription, accessibility

[View Template](./templates/speech-to-text-template.md) | [View Example](./examples/speech_to_text.py)

### 2. Speech to Text Translate
Transcribe and translate audio to English.

```python
response = client.speech_to_text.translate(
    file=open("audio.wav", "rb"),
    
)
```

**Use Cases:** International communication, content localization

[View Example](./examples/speech_to_text_translate.py)

### 3. Text to Speech
Generate natural-sounding speech from text.

```python
response = client.text_to_speech.convert(
    text="नमस्ते",
    target_language_code="hi-IN",
    speaker="meera"
)
```

**Use Cases:** Voice assistants, accessibility, audio content

[View Template](./templates/text-to-speech-template.md) | [View Example](./examples/text_to_speech.py)

### 4. Text Translation
Translate between Indian languages and English.

```python
response = client.text.translate(
    input="Hello",
    source_language_code="en-IN",
    target_language_code="hi-IN"
)
```

**Use Cases:** Localization, multilingual support, communication

[View Template](./templates/text-translation-template.md) | [View Example](./examples/text_translation.py)

### 5. Chat Completion
Conversational AI and text generation.

```python
response = client.chat.completions(
    messages=[
        {"role": "user", "content": "What is AI?"}
    ],
    model="sarvam-2b"
)
```

**Use Cases:** Chatbots, content generation, question answering

[View Template](./templates/chat-completion-template.md) | [View Example](./examples/chat_completion.py)

### 6. Document Intelligence
Extract text from PDFs and images with structure preservation in 23 languages.

```python
# Process document using REST API
import requests

# Create job
response = requests.post(
    "https://api.sarvam.ai/v1/document-intelligence/jobs",
    headers={"api-subscription-key": api_key},
    json={"language_code": "hi-IN", "output_format": "md"}
)
job_data = response.json()

# Upload file and process...
```

**Use Cases:** Document digitization, archival processing, invoice extraction

[View Template](./templates/document-intelligence-template.md) | [View Example](./examples/document_intelligence.py)

### 7. Vision API
Analyze images with captioning, OCR, and content extraction in 23 languages.

```python
from sarvamai import SarvamAI

client = SarvamAI(api_subscription_key=api_key)

# Option 1: Generate caption in Hindi
with open("image.jpg", "rb") as img:
    response = client.vision.analyze(
        file=img,
        prompt_type="caption_in",
        language="hi-IN"
    )
print(response.content)  # "एक सुंदर पहाड़ी दृश्य"

# Option 2: Extract text (OCR)
with open("document.jpg", "rb") as img:
    response = client.vision.analyze(
        file=img,
        prompt_type="default_ocr"
    )
print(response.content)  # Extracted text

# Option 3: Convert to markdown
with open("slide.jpg", "rb") as img:
    response = client.vision.analyze(
        file=img,
        prompt_type="extract_as_markdown"
    )
print(response.content)  # Markdown formatted content
```

**Prompt Types:**
- `caption_in`: Image captioning in 23 languages
- `default_ocr`: Text extraction from images
- `extract_as_markdown`: Convert image to markdown format

**Use Cases:** E-commerce descriptions, accessibility alt-text, document OCR, presentation conversion

[View Template](./templates/vision-template.md) | [View Example](./examples/vision.py)

## Supported Languages

| Language | Code | Speech-to-Text | Text-to-Speech | Translation | Document Intelligence | Vision |
|----------|------|----------------|----------------|-------------|----------------------|--------|
| Hindi | hi-IN | ✓ | ✓ | ✓ | ✓ | ✓ |
| English (Indian) | en-IN | ✓ | ✓ | ✓ | ✓ | ✓ |
| Bengali | bn-IN | ✓ | ✓ | ✓ | ✓ | ✓ |
| Gujarati | gu-IN | ✓ | ✓ | ✓ | ✓ | ✓ |
| Kannada | kn-IN | ✓ | ✓ | ✓ | ✓ | ✓ |
| Malayalam | ml-IN | ✓ | ✓ | ✓ | ✓ | ✓ |
| Marathi | mr-IN | ✓ | ✓ | ✓ | ✓ | ✓ |
| Odia | or-IN | ✓ | ✓ | ✓ | ✓ | ✓ |
| Punjabi | pa-IN | ✓ | ✓ | ✓ | ✓ | ✓ |
| Tamil | ta-IN | ✓ | ✓ | ✓ | ✓ | ✓ |
| Telugu | te-IN | ✓ | ✓ | ✓ | ✓ | ✓ |

**Document Intelligence and Vision support all 22 Indian languages + English (23 total)**

## Examples

### Multilingual Chatbot

```python
# Receive input in Hindi
user_input = "भारत की राजधानी क्या है?"

# Translate to English
translation = client.text.translate(
    input=user_input,
    source_language_code="hi-IN",
    target_language_code="en-IN"
)

# Get AI response
response = client.chat.completions(
    messages=[{"role": "user", "content": translation.translated_text}]
)

# Translate back to Hindi
final_response = client.text.translate(
    input=response.choices[0].message.content,
    source_language_code="en-IN",
    target_language_code="hi-IN"
)

# Convert to speech
audio = client.text_to_speech.convert(
    text=final_response.translated_text,
    target_language_code="hi-IN"
)
```

[View Full Example](./examples/end_to_end_example.py)

### Voice Assistant

```python
# 1. Record user audio
# 2. Transcribe to text
transcript = client.speech_to_text.transcribe(
    file=audio_file,
    
    language_code="hi-IN"
)

# 3. Process with AI
ai_response = client.chat.completions(
    messages=[{"role": "user", "content": transcript.transcript}]
)

# 4. Convert response to speech
speech = client.text_to_speech.convert(
    text=ai_response.choices[0].message.content,
    target_language_code="hi-IN"
)
```

### Content Localization

```python
# Localize content to multiple languages
original_content = "Welcome to our platform!"
languages = ["hi-IN", "ta-IN", "te-IN", "bn-IN"]

localized_content = {}
for lang in languages:
    # Translate
    translation = client.text.translate(
        input=original_content,
        source_language_code="en-IN",
        target_language_code=lang
    )
    
    # Generate audio
    audio = client.text_to_speech.convert(
        text=translation.translated_text,
        target_language_code=lang
    )
    
    localized_content[lang] = {
        "text": translation.translated_text,
        "audio": audio.audios[0]
    }
```

## Models

### Speech-to-Text Models
- **saarika:v2.5** - Latest transcription model with high accuracy
- **saaras:v2.5** - Transcription with translation to English

### Text-to-Speech Models
- **bulbul:v1** - Natural voice synthesis with multiple speakers

### Translation Models
- **mayura:v1** - Neural machine translation for Indian languages

### Chat Models
- **sarvam-2b** - Fast, lightweight model for simple tasks
- **sarvam-m** - Balanced model for general use
- **sarvam-1** - Full-featured model for complex tasks

### Document Intelligence Model
- **sarvam-vision** - 3B parameter VLM for document processing in 23 languages

## Best Practices

### 1. API Key Security
```python
# ✓ Good - Use environment variables
api_key = os.getenv("SARVAM_API_KEY")

# ✗ Bad - Hardcoded key
api_key = "your_key_here"
```

### 2. Error Handling
```python
try:
    response = client.text.translate(...)
except Exception as e:
    print(f"Error: {e}")
    # Implement retry logic or fallback
```

### 3. Optimize Token Usage
```python
# Monitor usage
response = client.chat.completions(...)
print(f"Tokens used: {response.usage.total_tokens}")
```

### 4. Choose the Right Model
- Use `sarvam-2b` for fast, simple responses
- Use `sarvam-m` for balanced performance
- Use `sarvam-1` for complex reasoning

## Use Cases

### Customer Support
- Multilingual chatbots
- Voice-based support
- Automated translations

### Education
- Language learning tools
- Interactive tutors
- Multilingual content

### Accessibility
- Text-to-speech readers
- Voice interfaces
- Transcription services

### Content Creation
- Automated translation
- Audio generation
- Content localization

### Healthcare
- Patient communication
- Medical transcription
- Multilingual information

## Getting Help

- **Documentation**: [docs.sarvam.ai](https://docs.sarvam.ai)
- **API Reference**: [API Docs](https://docs.sarvam.ai/api-reference-docs)
- **Discord**: [Join Community](https://discord.com/invite/5rAsykttcs)
- **Dashboard**: [dashboard.sarvam.ai](https://dashboard.sarvam.ai)
- **Examples**: Check the [examples/](./examples/) directory
- **Templates**: Browse the [templates/](./templates/) directory

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch
3. Add your examples or templates
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Resources

- [Sarvam AI Website](https://sarvam.ai)
- [API Documentation](https://docs.sarvam.ai)
- [Python SDK on PyPI](https://pypi.org/project/sarvamai/)
- [JavaScript SDK on npm](https://www.npmjs.com/package/sarvamai)
- [Cookbook Examples](https://docs.sarvam.ai/api-reference-docs/cookbook)
- [Discord Community](https://discord.com/invite/5rAsykttcs)

## Acknowledgments

Built with ❤️ for Indian language AI applications using [Sarvam AI](https://sarvam.ai).

---

**Note**: This is an unofficial collection of skills and templates. For official documentation, visit [docs.sarvam.ai](https://docs.sarvam.ai).
