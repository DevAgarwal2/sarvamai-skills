# Sarvam AI Text-to-Speech Skill Template

**Last Updated:** February 2026
**API Version:** bulbul:v3 (default)

## Overview
Convert text into natural-sounding speech in Indian languages using Sarvam AI's text-to-speech API.

## API Information

**Endpoint:** `https://api.sarvam.ai/text-to-speech`
**Method:** POST
**Model:** bulbul:v3 (default)

## Available Model

### bulbul:v3 (Default)
- **Max text length:** 2500 characters
- **Default sample rate:** 24000 Hz
- **Speakers:** 45 voices
- **Supports:** pace, temperature control
- **Note:** pitch and loudness NOT supported

## Supported Languages

All 11 Indian languages:
- Hindi (hi-IN), Bengali (bn-IN), English (en-IN)
- Gujarati (gu-IN), Kannada (kn-IN), Malayalam (ml-IN)
- Marathi (mr-IN), Odia (od-IN), Punjabi (pa-IN)
- Tamil (ta-IN), Telugu (te-IN)

## Available Speakers

### bulbul:v3 Speakers (45 total)

**Default:** aditya

**All speakers:**
- Male: aditya (default), shubh, rahul, rohan, amit, dev, ratan, varun, manan, sumit, kabir, aayan, ashutosh, advait, anand, tarun, sunny, mani, gokul, vijay, mohit, rehan, soham, abhilash, karun, hitesh
- Female: ritu, priya, neha, pooja, simran, kavya, ishita, shreya, roopa, amelia, sophia, tanya, shruti, suhani, kavitha, rupali, anushka, manisha, vidya, arya

## Response Format

```json
{
  "request_id": "req_123",
  "audios": ["base64_encoded_audio_data"]
}
```

Audio is returned as base64-encoded WAV data.

## Python Examples

### Example 1: Basic TTS (bulbul:v3)

```python
from sarvamai import SarvamAI
import os
import base64

client = SarvamAI(api_subscription_key=os.getenv("SARVAM_API_KEY"))

response = client.text_to_speech.convert(
    text="नमस्ते, सर्वम AI में आपका स्वागत है",
    target_language_code="hi-IN",
    model="bulbul:v3",
    speaker="shubh"
)

# Save audio file
audio_data = base64.b64decode(response.audios[0])
with open("output.wav", "wb") as f:
    f.write(audio_data)
```

### Example 2: Custom Parameters (bulbul:v3)

```python
response = client.text_to_speech.convert(
    text="Welcome to Sarvam AI!",
    target_language_code="en-IN",
    model="bulbul:v3",
    speaker="aditya",
    pace=1.2,           # Faster speed
    temperature=0.7,   # Control randomness/expressiveness
    speech_sample_rate=24000
)
```

## TypeScript Example

```typescript
import { SarvamAIClient } from "sarvamai";
import * as fs from "fs";

const client = new SarvamAIClient({ 
  apiSubscriptionKey: process.env.SARVAM_API_KEY 
});

const response = await client.textToSpeech.convert({
  text: "Hello from Sarvam AI!",
  target_language_code: "en-IN",
  model: "bulbul:v2",
  speaker: "anushka"
});

console.log(response);
```

## cURL Example

```bash
curl -X POST https://api.sarvam.ai/text-to-speech \
  -H "api-subscription-key: YOUR_SARVAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Welcome to Sarvam AI!",
    "target_language_code": "hi-IN",
    "model": "bulbul:v3",
    "speaker": "shubh",
    "pace": 1.0,
    "temperature": 0.6
  }'
```

## Use Cases

1. **Accessibility** - Convert text to audio for visually impaired users
2. **Voice Assistants** - Generate voice responses in Indian languages
3. **Audio Books** - Create audiobook versions of written content
4. **E-Learning** - Generate audio lessons in regional languages
5. **IVR Systems** - Interactive voice response for customer service
6. **Content Localization** - Multi-language audio content

## Voice Customization Guide

### bulbul:v3 Parameters

**Pace:**
- `0.5-0.7`: Slow, deliberate
- `1.0`: Natural speed
- `1.5-2.0`: Fast, energetic

**Temperature:**
- `0.01-0.3`: Focused, consistent
- `0.6`: Balanced (default)
- `0.8-2.0`: More varied, natural

## Model Selection Guide

**Use bulbul:v3 when:**
- Need longer text support (up to 2500 chars)
- Want more natural variation (temperature control)
- Need access to 45 different speakers
- Higher quality output

## Best Practices

1. **Text Length:** Split long texts into chunks (2500 max for bulbul:v3)
2. **Sample Rate:** Use 24000 Hz for production
3. **Speaker Selection:** Test different voices for your use case
4. **Temperature:** Adjust between 0.3-0.8 for optimal expressiveness

## Common Errors

| Error | Solution |
|-------|----------|
| 401 Unauthorized | Check API key |
| 400 Bad Request | Verify parameters for model version |
| 422 Unprocessable Entity | Check text language matches target_language_code |
| 413 Payload Too Large | Reduce text length (2500 max for bulbul:v3) |

## Parameter Compatibility (bulbul:v3)

| Parameter | Supported | Range | Description |
|-----------|-----------|-------|-------------|
| pace | ✅ Yes | 0.5 to 2.0 | Speaking speed |
| temperature | ✅ Yes | 0.01 to 2.0 | Expressiveness/randomness |
| pitch | ❌ No | - | Not supported in v3 |
| loudness | ❌ No | - | Not supported in v3 |

## Resources

- [API Documentation](https://docs.sarvam.ai/api-reference-docs/text-to-speech/convert)
- [Voice Samples](https://docs.sarvam.ai/api-reference-docs/api-guides-tutorials/text-to-speech/overview)
- [Python SDK](https://pypi.org/project/sarvamai/)
- [Dashboard](https://dashboard.sarvam.ai)
- [API Versions Reference](./API_VERSIONS.md)
