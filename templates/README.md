# Sarvam AI Skills Templates

This directory contains comprehensive templates for creating skills using Sarvam AI APIs.

## Available Templates

### 1. [Speech-to-Text Template](./speech-to-text-template.md)
Template for creating audio transcription skills in Indian languages.

**Key Features:**
- Audio transcription in 11+ Indian languages
- Model: saarika:v2.5
- Use cases: Voice notes, meetings, accessibility

### 2. [Text-to-Speech Template](./text-to-speech-template.md)
Template for creating text-to-speech conversion skills.

**Key Features:**
- Natural voice synthesis
- Multiple speakers and voices
- Voice customization (pitch, pace, loudness)
- Model: bulbul:v1

### 3. [Text Translation Template](./text-translation-template.md)
Template for building translation skills between Indian languages.

**Key Features:**
- Auto language detection
- 10+ language pairs
- Formal/informal modes
- Gender-aware translation
- Model: mayura:v1

### 4. [Chat Completion Template](./chat-completion-template.md)
Template for conversational AI and text generation skills.

**Key Features:**
- Multiple model sizes (sarvam-2b, sarvam-m, sarvam-1)
- Multi-turn conversations
- Temperature tuning
- Streaming support

### 5. [General Skill Template](./skill-template.md)
Basic template for creating any Sarvam AI skill.

## How to Use These Templates

### Step 1: Choose the Right Template
Select the template that matches your use case:
- **Speech to Text**: Audio transcription needs
- **Text to Speech**: Audio generation needs
- **Translation**: Cross-language communication
- **Chat**: Conversational AI or content generation

### Step 2: Read the Template
Each template includes:
- API overview and endpoints
- Request/response formats
- Code examples (Python, cURL)
- Best practices
- Common use cases
- Error handling

### Step 3: Customize for Your Skill
- Adapt the code examples to your specific needs
- Configure parameters based on your requirements
- Implement error handling
- Add your business logic

### Step 4: Test Thoroughly
- Test with various inputs
- Handle edge cases
- Monitor API usage and costs
- Validate outputs

## Template Structure

Each template follows this structure:

```markdown
# API Overview
- Endpoint information
- Supported features
- Model details

# Parameters
- Request parameters
- Response format
- Examples

# Code Examples
- Python SDK examples
- cURL examples
- Advanced patterns

# Use Cases
- Common applications
- Industry examples

# Best Practices
- Optimization tips
- Error handling
- Performance tuning

# Resources
- Documentation links
- Additional references
```

## Quick Start Example

Here's a quick example combining multiple APIs:

```python
from sarvamai import SarvamAI
import os

# Initialize client
client = SarvamAI(api_subscription_key=os.getenv("SARVAM_API_KEY"))

# 1. Translate text
translation = client.text.translate(
    input="Hello, world!",
    source_language_code="en-IN",
    target_language_code="hi-IN"
)

# 2. Convert to speech
audio = client.text_to_speech.convert(
    text=translation.translated_text,
    target_language_code="hi-IN"
)

# 3. Get AI response
response = client.chat.completions(
    messages=[
        {"role": "user", "content": "Explain this in simple terms"}
    ]
)
```

## Skill Design Patterns

### Pattern 1: Speech-to-Text-to-Action
```
Audio Input → Transcribe → Process Text → Take Action
```

### Pattern 2: Multilingual Chatbot
```
User Input (any language) → Translate to English → Chat AI → Translate Back → Respond
```

### Pattern 3: Content Localization
```
Original Content → Translate → Convert to Speech → Distribute
```

### Pattern 4: Voice Assistant
```
Voice Input → Transcribe → Chat AI → Generate Response → Text to Speech
```

## Language Support Matrix

| Language | Code | STT | TTS | Translation | Chat |
|----------|------|-----|-----|-------------|------|
| Hindi | hi-IN | ✓ | ✓ | ✓ | ✓ |
| English | en-IN | ✓ | ✓ | ✓ | ✓ |
| Bengali | bn-IN | ✓ | ✓ | ✓ | ✓ |
| Gujarati | gu-IN | ✓ | ✓ | ✓ | ✓ |
| Kannada | kn-IN | ✓ | ✓ | ✓ | ✓ |
| Malayalam | ml-IN | ✓ | ✓ | ✓ | ✓ |
| Marathi | mr-IN | ✓ | ✓ | ✓ | ✓ |
| Odia | or-IN | ✓ | ✓ | ✓ | ✓ |
| Punjabi | pa-IN | ✓ | ✓ | ✓ | ✓ |
| Tamil | ta-IN | ✓ | ✓ | ✓ | ✓ |
| Telugu | te-IN | ✓ | ✓ | ✓ | ✓ |

## Common Skill Types

### Customer Support Bot
- Text/voice input
- Multilingual support
- Chat completion for responses
- Text-to-speech for voice responses

### Content Creator
- Text generation with chat API
- Translation to multiple languages
- Text-to-speech for audio content

### Accessibility Tool
- Speech-to-text for input
- Text processing
- Text-to-speech for output

### Educational Assistant
- Multilingual support
- Interactive conversations
- Content generation
- Voice interaction

## Best Practices Across All Skills

1. **API Key Security**
   - Use environment variables
   - Never commit API keys
   - Rotate keys regularly

2. **Error Handling**
   - Implement retry logic
   - Handle rate limits
   - Provide user feedback

3. **Performance**
   - Cache common translations
   - Batch requests when possible
   - Monitor token usage

4. **Quality**
   - Validate inputs
   - Test edge cases
   - Monitor outputs

5. **Cost Optimization**
   - Choose appropriate models
   - Optimize token usage
   - Implement caching

## Resources

- [Sarvam AI Documentation](https://docs.sarvam.ai)
- [API Reference](https://docs.sarvam.ai/api-reference-docs)
- [Python SDK](https://pypi.org/project/sarvamai/)
- [Dashboard](https://dashboard.sarvam.ai)
- [Examples Directory](../examples/)

## Getting Help

- Check the [examples](../examples/) for working code
- Read the [API documentation](https://docs.sarvam.ai)
- Join the [Discord community](https://discord.com/invite/5rAsykttcs)
- Review error codes in individual templates

## Contributing

To contribute a new template:

1. Follow the existing template structure
2. Include comprehensive examples
3. Document all parameters
4. Provide use cases
5. Add best practices
6. Test all code examples
