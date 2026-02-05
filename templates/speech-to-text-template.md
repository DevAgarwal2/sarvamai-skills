# Sarvam AI Speech-to-Text Skill Template

## Overview
This template helps you create skills that use Sarvam AI's speech-to-text (transcription) API to convert audio in Indian languages to text.

## API Information

**Endpoint:** `https://api.sarvam.ai/speech-to-text`  
**Method:** POST  
**Models:** 
- `saarika:v2.5` - Standard transcription (default)
- `saaras:v3` - Advanced multi-mode transcription (NEW)

## Available Models

| Model | Modes | Description |
|-------|-------|-------------|
| saarika:v2.5 | transcribe | Standard speech-to-text transcription |
| saaras:v3 | transcribe, translate, verbatim, translit, codemix | Advanced model with 5 specialized modes |

## saaras:v3 Modes

| Mode | Output | Use Case |
|------|--------|----------|
| transcribe | Clean transcript in source language | Standard transcription, removes filler words |
| translate | English translation | Transcribe and translate to English in one step |
| verbatim | Word-for-word including fillers | Meeting minutes, legal transcription |
| translit | Transliterated text (Roman script) | Non-native script users |
| codemix | Mixed language transcript | Code-switched conversations (e.g., Hinglish) |

## Supported Languages

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

## Request Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| file | File | Yes | - | Audio file (WAV, MP3, etc.) |
| model | String | Yes | - | Model name: "saarika:v2.5" or "saaras:v3" |
| language_code | String | Yes | - | Language code (e.g., "hi-IN", "en-IN") |
| mode | String | No | transcribe | Mode for saaras:v3 (transcribe/translate/verbatim/translit/codemix) |

## Response Format

```json
{
  "transcript": "transcribed text here",
  "language_code": "hi-IN"
}
```

## Python Example

### Using saarika:v2.5 (Standard)
```python
from sarvamai import SarvamAI
import os

client = SarvamAI(
    api_subscription_key=os.getenv("SARVAM_API_KEY")
)

with open("audio.wav", "rb") as audio_file:
    response = client.speech_to_text.transcribe(
        file=audio_file,
        model="saarika:v2.5",
        language_code="hi-IN"
    )

print(response.transcript)
```

### Using saaras:v3 (Advanced with Modes)
```python
# Mode 1: Standard transcription (clean)
with open("audio.wav", "rb") as audio_file:
    response = client.speech_to_text.transcribe(
        file=audio_file,
        model="saaras:v3",
        language_code="hi-IN",
        mode="transcribe"
    )
    print("Transcript:", response.transcript)

# Mode 2: Transcribe + Translate to English
with open("audio.wav", "rb") as audio_file:
    response = client.speech_to_text.transcribe(
        file=audio_file,
        model="saaras:v3",
        language_code="hi-IN",
        mode="translate"
    )
    print("English Translation:", response.transcript)

# Mode 3: Verbatim (includes filler words)
with open("audio.wav", "rb") as audio_file:
    response = client.speech_to_text.transcribe(
        file=audio_file,
        model="saaras:v3",
        language_code="hi-IN",
        mode="verbatim"
    )
    print("Verbatim:", response.transcript)

# Mode 4: Transliteration (Roman script)
with open("audio.wav", "rb") as audio_file:
    response = client.speech_to_text.transcribe(
        file=audio_file,
        model="saaras:v3",
        language_code="hi-IN",
        mode="translit"
    )
    print("Transliterated:", response.transcript)

# Mode 5: Code-mixed (for Hinglish, etc.)
with open("audio.wav", "rb") as audio_file:
    response = client.speech_to_text.transcribe(
        file=audio_file,
        model="saaras:v3",
        language_code="hi-IN",
        mode="codemix"
    )
    print("Code-mixed:", response.transcript)
```

## cURL Example

### saarika:v2.5
```bash
curl -X POST https://api.sarvam.ai/speech-to-text \
  -H "api-subscription-key: YOUR_SARVAM_API_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F model="saarika:v2.5" \
  -F language_code="hi-IN" \
  -F file=@"audio.wav;type=audio/wav"
```

### saaras:v3 with mode
```bash
curl -X POST https://api.sarvam.ai/speech-to-text \
  -H "api-subscription-key: YOUR_SARVAM_API_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F model="saaras:v3" \
  -F language_code="hi-IN" \
  -F mode="translate" \
  -F file=@"audio.wav;type=audio/wav"
```

## Use Cases

### saarika:v2.5
1. **Voice Transcription**: Convert recorded voice notes to text
2. **Meeting Notes**: Basic meeting transcription
3. **Content Creation**: Convert audio content to text for editing
4. **Voice Commands**: Process voice commands in regional languages

### saaras:v3 Specific Use Cases

**Transcribe Mode:**
- Clean transcription for documentation
- Removing filler words ("um", "uh", etc.)
- Professional content creation

**Translate Mode:**
- Real-time translation to English
- International communication
- Cross-language content creation

**Verbatim Mode:**
- Legal depositions and court proceedings
- Detailed meeting minutes
- Research interviews
- Compliance documentation

**Translit Mode:**
- Users without native script keyboards
- Learning native languages
- SMS and messaging in Roman script

**Codemix Mode:**
- Hinglish conversations
- Mixed language customer support
- Urban multilingual contexts

## Mode Comparison Examples

### Input Audio (Hindi)
"नमस्ते, मैं, उम्म, आज दिल्ली जा रहा हूं और वहां meeting attend करूंगा।"

### Output by Mode

**transcribe:**
```
"नमस्ते, मैं आज दिल्ली जा रहा हूं और वहां मीटिंग अटेंड करूंगा।"
```
(Clean, native script, filler removed)

**translate:**
```
"Hello, I am going to Delhi today and will attend a meeting there."
```
(English translation)

**verbatim:**
```
"नमस्ते, मैं, उम्म, आज दिल्ली जा रहा हूं और वहां meeting attend करूंगा।"
```
(Exact words including "उम्म", keeps English words as-is)

**translit:**
```
"Namaste, main aaj Delhi ja raha hoon aur wahan meeting attend karunga."
```
(Roman script transliteration)

**codemix:**
```
"नमस्ते, मैं आज दिल्ली जा रहा हूं और वहां meeting attend करूंगा।"
```
(Preserves code-mixed nature, Hindi in Devanagari + English words)

## Best Practices

1. **Model Selection**: 
   - Use `saarika:v2.5` for simple transcription
   - Use `saaras:v3` when you need modes (translate, verbatim, etc.)
2. **Mode Selection**: Choose the appropriate mode based on your use case
3. **Audio Quality**: Use clear audio with minimal background noise
4. **File Format**: WAV format recommended for best results
5. **Language Selection**: Specify correct language code for better accuracy
6. **File Size**: Keep audio files under 25MB
7. **Error Handling**: Always implement error handling for failed requests

## Common Errors

| Error | Solution |
|-------|----------|
| 401 Unauthorized | Check API key is valid |
| 400 Bad Request | Verify file format and parameters |
| 413 Payload Too Large | Reduce audio file size |
| 422 Unprocessable Entity | Check language code is supported |

## Skill Template Structure

When creating a skill using this API:

1. Define the skill purpose (e.g., "transcribe meeting recordings")
2. Specify required inputs (audio file, language)
3. Configure API parameters
4. Handle the response appropriately
5. Include error handling
6. Add user feedback mechanisms

## Related APIs

- **Speech to Text Translate (saaras:v3)**: Now integrated as "translate" mode
- **Text to Speech**: Convert the transcribed text back to audio
- **Chat Completion**: Process transcribed text with AI
- **Translation**: Further process transcripts in different languages

## Resources

- [API Documentation](https://docs.sarvam.ai/api-reference-docs/endpoints/speech-to-text)
- [Python SDK](https://pypi.org/project/sarvamai/)
- [Dashboard](https://dashboard.sarvam.ai)
