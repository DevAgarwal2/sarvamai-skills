# Sarvam AI Text-to-Speech Skill Template

**Last Updated:** February 2026  
**API Version:** bulbul:v2 (default), bulbul:v3-beta

## Overview
Convert text into natural-sounding speech in Indian languages using Sarvam AI's text-to-speech API.

## API Information

**Endpoint:** `https://api.sarvam.ai/text-to-speech`  
**Method:** POST  
**Models:** bulbul:v2 (default), bulbul:v3-beta

## Available Models

### bulbul:v2 (Default)
- **Max text length:** 1500 characters
- **Default sample rate:** 22050 Hz
- **Speakers:** 7 voices
- **Supports:** pitch, pace, loudness control

### bulbul:v3-beta (New)
- **Max text length:** 2500 characters
- **Default sample rate:** 24000 Hz
- **Speakers:** 31 voices
- **Supports:** pace, temperature control
- **Note:** pitch and loudness NOT supported

## Supported Languages

All 11 Indian languages:
- Hindi (hi-IN), Bengali (bn-IN), English (en-IN)
- Gujarati (gu-IN), Kannada (kn-IN), Malayalam (ml-IN)
- Marathi (mr-IN), Odia (od-IN), Punjabi (pa-IN)
- Tamil (ta-IN), Telugu (te-IN)

## Available Speakers

### bulbul:v2 Speakers (7 total)

**Female Voices:**
- **anushka** (default) - Clear and professional
- **manisha** - Warm and friendly
- **vidya** - Articulate and precise
- **arya** - Young and energetic

**Male Voices:**
- **abhilash** - Deep and authoritative
- **karun** - Natural and conversational
- **hitesh** - Professional and engaging

### bulbul:v3-beta Speakers (31 total)

**Default:** aditya

**All speakers:** aditya, ritu, priya, neha, rahul, pooja, rohan, simran, kavya, amit, dev, ishita, shreya, ratan, varun, manan, sumit, roopa, kabir, aayan, shubh, ashutosh, advait, amelia, sophia

## Request Parameters

### Common Parameters (Both Models)

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| text | String | Yes | Text to convert (max 1500 for v2, 2500 for v3-beta) |
| target_language_code | String | Yes | Language code (hi-IN, en-IN, etc.) |
| model | String | No | bulbul:v2 (default) or bulbul:v3-beta |
| speaker | String | No | Speaker name (default: anushka for v2, aditya for v3-beta) |

### bulbul:v2 Specific

| Parameter | Type | Default | Range | Description |
|-----------|------|---------|-------|-------------|
| pitch | Float | 0.0 | -0.75 to 0.75 | Voice pitch |
| pace | Float | 1.0 | 0.3 to 3.0 | Speaking speed |
| loudness | Float | 1.0 | 0.3 to 3.0 | Audio volume |
| speech_sample_rate | Integer | 22050 | 8000/16000/22050/24000 | Sample rate Hz |
| enable_preprocessing | Boolean | false | - | Normalize numbers/dates |

### bulbul:v3-beta Specific

| Parameter | Type | Default | Range | Description |
|-----------|------|---------|-------|-------------|
| pace | Float | 1.0 | 0.5 to 2.0 | Speaking speed (narrower range) |
| temperature | Float | 0.6 | 0.01 to 1.0 | Output randomness |
| speech_sample_rate | Integer | 24000 | 8000/16000/22050/24000 | Sample rate Hz |
| enable_preprocessing | Boolean | true | - | Always enabled |

**⚠️ Important:** pitch and loudness are NOT supported in bulbul:v3-beta

## Response Format

```json
{
  "request_id": "req_123",
  "audios": ["base64_encoded_audio_data"]
}
```

Audio is returned as base64-encoded WAV data.

## Python Examples

### Example 1: Basic TTS (bulbul:v2)

```python
from sarvamai import SarvamAI
import os
import base64

client = SarvamAI(api_subscription_key=os.getenv("SARVAM_API_KEY"))

response = client.text_to_speech.convert(
    text="नमस्ते, सर्वम AI में आपका स्वागत है",
    target_language_code="hi-IN",
    model="bulbul:v2",
    speaker="anushka"
)

# Save audio file
audio_data = base64.b64decode(response.audios[0])
with open("output.wav", "wb") as f:
    f.write(audio_data)
```

### Example 2: Custom Voice Control (bulbul:v2)

```python
response = client.text_to_speech.convert(
    text="Welcome to Sarvam AI!",
    target_language_code="en-IN",
    model="bulbul:v2",
    speaker="abhilash",
    pitch=0.5,        # Higher pitch
    pace=1.3,         # Faster speed
    loudness=1.8      # Louder volume
)
```

### Example 3: Using bulbul:v3-beta

```python
response = client.text_to_speech.convert(
    text="यह बल्बुल v3-बीटा मॉडल का उपयोग कर रहा है",
    target_language_code="hi-IN",
    model="bulbul:v3-beta",
    speaker="aditya",
    pace=1.2,
    temperature=0.7    # Control randomness
)
# Note: pitch and loudness NOT supported in v3-beta
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
    "model": "bulbul:v2",
    "speaker": "anushka",
    "pace": 1.0,
    "pitch": 0.0,
    "loudness": 1.5
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

### bulbul:v2 Parameters

**Pitch:**
- `-0.75 to -0.5`: Deeper voice
- `0.0`: Natural pitch
- `0.5 to 0.75`: Higher voice

**Pace:**
- `0.3-0.7`: Slow, deliberate
- `1.0`: Natural speed
- `1.5-3.0`: Fast, energetic

**Loudness:**
- `0.3-0.8`: Quiet
- `1.0-1.5`: Normal
- `2.0-3.0`: Loud

### bulbul:v3-beta Parameters

**Temperature:**
- `0.01-0.3`: Focused, consistent
- `0.6`: Balanced (default)
- `0.8-1.0`: More varied, natural

## Model Selection Guide

**Choose bulbul:v2 when:**
- Need precise voice control (pitch, loudness)
- Shorter texts (under 1500 chars)
- Want specific voice characteristics

**Choose bulbul:v3-beta when:**
- Need longer text support (up to 2500 chars)
- Want more natural variation (temperature control)
- Need access to 31 different speakers
- Higher quality output

## Best Practices

1. **Text Length:** Split long texts into chunks (1500 for v2, 2500 for v3-beta)
2. **Preprocessing:** Enable for better number/date pronunciation
3. **Sample Rate:** Use 22050 Hz (v2) or 24000 Hz (v3-beta) for production
4. **Speaker Selection:** Test different voices for your use case
5. **Model Selection:** Use correct parameters for each model version

## Common Errors

| Error | Solution |
|-------|----------|
| 401 Unauthorized | Check API key |
| 400 Bad Request | Verify parameters for model version |
| 422 Unprocessable Entity | Check text language matches target_language_code |
| 413 Payload Too Large | Reduce text length (1500 for v2, 2500 for v3-beta) |

## Parameter Compatibility

| Parameter | bulbul:v2 | bulbul:v3-beta |
|-----------|-----------|----------------|
| pitch | ✅ Yes | ❌ No |
| pace | ✅ Yes (0.3-3.0) | ✅ Yes (0.5-2.0) |
| loudness | ✅ Yes | ❌ No |
| temperature | ❌ No | ✅ Yes |
| preprocessing | Optional | Always enabled |

## Resources

- [API Documentation](https://docs.sarvam.ai/api-reference-docs/text-to-speech/convert)
- [Voice Samples](https://docs.sarvam.ai/api-reference-docs/api-guides-tutorials/text-to-speech/overview)
- [Python SDK](https://pypi.org/project/sarvamai/)
- [Dashboard](https://dashboard.sarvam.ai)
- [API Versions Reference](./API_VERSIONS.md)
