# Sarvam AI Text Translation Skill Template

## Overview
This template helps you create skills that use Sarvam AI's translation API to translate text between various Indian languages and English.

## API Information

**Endpoint:** `https://api.sarvam.ai/translate`  
**Method:** POST  
**Models:** 
- `mayura:v1` - Supports 11 languages
- `sarvam-translate:v1` - Supports 22 languages (recommended)

## Available Models

| Model | Languages | Status | Description |
|-------|-----------|--------|-------------|
| mayura:v1 | 11 | Stable | Original translation model |
| sarvam-translate:v1 | 22 | Recommended | Extended language support including Assamese, Urdu, Sanskrit, etc. |

## Supported Languages

### mayura:v1 (11 Languages)

Translation supported between any pair of these 11 languages:

- Hindi (hi-IN)
- English (en-IN)
- Bengali (bn-IN)
- Gujarati (gu-IN)
- Kannada (kn-IN)
- Malayalam (ml-IN)
- Marathi (mr-IN)
- Odia (or-IN)
- Punjabi (pa-IN)
- Tamil (ta-IN)
- Telugu (te-IN)

### sarvam-translate:v1 (22 Languages - Recommended)

Translation supported between any pair of these 22 languages:

**Original 11:**
- Hindi (hi-IN)
- English (en-IN)
- Bengali (bn-IN)
- Gujarati (gu-IN)
- Kannada (kn-IN)
- Malayalam (ml-IN)
- Marathi (mr-IN)
- Odia (or-IN)
- Punjabi (pa-IN)
- Tamil (ta-IN)
- Telugu (te-IN)

**Additional 11 (sarvam-translate:v1 only):**
- Assamese (as-IN)
- Bodo (brx-IN)
- Dogri (doi-IN)
- Konkani (gom-IN)
- Kashmiri (ks-IN)
- Maithili (mai-IN)
- Manipuri (mni-IN)
- Nepali (ne-IN)
- Sanskrit (sa-IN)
- Santali (sat-IN)
- Sindhi (sd-IN)
- Urdu (ur-IN)

## Request Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| input | String | Yes | - | Text to translate |
| source_language_code | String | Yes | - | Source language code (use "auto" for auto-detection) |
| target_language_code | String | Yes | - | Target language code |
| speaker_gender | String | No | Male | Gender for context (Male/Female) |
| mode | String | No | formal | Translation formality (formal/informal) |
| model | String | No | sarvam-translate:v1 | Translation model (mayura:v1 or sarvam-translate:v1) |
| enable_preprocessing | Boolean | No | false | Enable text preprocessing |

## Response Format

```json
{
  "translated_text": "translated output here"
}
```

## Python Example

```python
from sarvamai import SarvamAI
import os

client = SarvamAI(
    api_subscription_key=os.getenv("SARVAM_API_KEY")
)

# Using sarvam-translate:v1 (22 languages)
response = client.text.translate(
    input="Hello, how are you?",
    source_language_code="en-IN",
    target_language_code="hi-IN",
    speaker_gender="Male",
    mode="formal",
    model="sarvam-translate:v1"
)

print(response.translated_text)
```

## cURL Example

```bash
curl -X POST https://api.sarvam.ai/translate \
  -H "api-subscription-key: YOUR_SARVAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input": "Hello, how are you?",
    "source_language_code": "en-IN",
    "target_language_code": "hi-IN",
    "model": "sarvam-translate:v1"
  }'
```

## Use Cases

1. **Content Localization**: Translate website content to regional languages
2. **Document Translation**: Convert documents between Indian languages
3. **Customer Support**: Provide multilingual support
4. **Education**: Translate learning materials
5. **E-commerce**: Localize product descriptions
6. **Social Media**: Translate posts and comments
7. **Communication**: Enable cross-language communication

## Auto Language Detection

Use "auto" as source_language_code to automatically detect the input language:

```python
response = client.text.translate(
    input="ನಮಸ್ಕಾರ",  # Input in Kannada
    source_language_code="auto",  # Auto-detect
    target_language_code="en-IN",
    model="sarvam-translate:v1"
)
```

## Model Comparison

### When to use mayura:v1
- Need to translate between the original 11 languages only
- Proven stable performance
- Legacy applications

### When to use sarvam-translate:v1 (Recommended)
- Need support for additional languages (Assamese, Urdu, Sanskrit, etc.)
- Building new applications
- Require broader language coverage
- All 22 Indian languages supported

## Extended Language Examples

Using sarvam-translate:v1 to access additional languages:

```python
# English to Urdu
urdu_response = client.text.translate(
    input="Welcome to our service",
    source_language_code="en-IN",
    target_language_code="ur-IN",
    model="sarvam-translate:v1"
)

# Sanskrit to English
sanskrit_response = client.text.translate(
    input="स्वागतम्",
    source_language_code="sa-IN",
    target_language_code="en-IN",
    model="sarvam-translate:v1"
)

# Assamese to Hindi
assamese_response = client.text.translate(
    input="আপোনাক স্বাগতম",
    source_language_code="as-IN",
    target_language_code="hi-IN",
    model="sarvam-translate:v1"
)
```

## Translation Modes

### Formal Mode
Use for professional, business, or official content:
```python
response = client.text.translate(
    input="How are you?",
    source_language_code="en-IN",
    target_language_code="hi-IN",
    mode="formal"
)
# Output: "आप कैसे हैं?"
```

### Informal Mode
Use for casual, friendly conversations:
```python
response = client.text.translate(
    input="How are you?",
    source_language_code="en-IN",
    target_language_code="hi-IN",
    mode="informal"
)
# Output: "तुम कैसे हो?"
```

## Gender Context

The speaker_gender parameter helps provide appropriate translations in gender-specific languages:

```python
# Male context
male_response = client.text.translate(
    input="I am happy",
    source_language_code="en-IN",
    target_language_code="hi-IN",
    speaker_gender="Male"
)

# Female context
female_response = client.text.translate(
    input="I am happy",
    source_language_code="en-IN",
    target_language_code="hi-IN",
    speaker_gender="Female"
)
```

## Best Practices

1. **Language Detection**: Use "auto" when source language is unknown
2. **Context Matters**: Choose appropriate mode (formal/informal) based on use case
3. **Gender Awareness**: Specify speaker_gender for accurate translations
4. **Batch Translation**: Translate multiple texts in parallel for efficiency
5. **Text Length**: Keep segments under 5000 characters
6. **Quality Check**: Review translations for context-specific terms

## Common Translation Patterns

### Website Localization
```python
def translate_website_content(content, target_lang):
    translations = {}
    for key, text in content.items():
        response = client.text.translate(
            input=text,
            source_language_code="en-IN",
            target_language_code=target_lang,
            mode="formal"
        )
        translations[key] = response.translated_text
    return translations
```

### Multilingual Chat
```python
def translate_message(message, from_lang, to_lang):
    response = client.text.translate(
        input=message,
        source_language_code=from_lang,
        target_language_code=to_lang,
        mode="informal"
    )
    return response.translated_text
```

## Common Errors

| Error | Solution |
|-------|----------|
| 401 Unauthorized | Check API key is valid |
| 400 Bad Request | Verify language codes are correct |
| 422 Unprocessable Entity | Check text is valid for source language |
| 413 Payload Too Large | Reduce text length |

## Skill Template Structure

When creating a translation skill:

1. Identify source and target languages
2. Determine appropriate mode (formal/informal)
3. Handle auto-detection if needed
4. Implement batch translation for multiple texts
5. Add caching for frequently translated content
6. Include error handling and fallbacks

## Language Pairs

Popular translation pairs:

- **English ↔ Hindi**: Most common use case
- **English ↔ Tamil**: South Indian content
- **Hindi ↔ Bengali**: Inter-regional communication
- **English ↔ Multiple**: Content localization
- **Auto → English**: Universal understanding

## Advanced Features

### Batch Translation
```python
texts = ["Hello", "Goodbye", "Thank you"]
translations = []

for text in texts:
    response = client.text.translate(
        input=text,
        source_language_code="en-IN",
        target_language_code="hi-IN"
    )
    translations.append(response.translated_text)
```

### Translation Pipeline
Combine with other APIs:
1. Translate text to target language
2. Convert to speech with TTS
3. Create multilingual audio content

## Related APIs

- **Text to Speech**: Convert translated text to audio
- **Speech to Text Translate**: Direct audio translation
- **Chat Completion**: Generate content in multiple languages

## Resources

- [API Documentation](https://docs.sarvam.ai/api-reference-docs/endpoints/translate)
- [Supported Languages](https://docs.sarvam.ai/languages)
- [Python SDK](https://pypi.org/project/sarvamai/)
- [Dashboard](https://dashboard.sarvam.ai)
