# Sarvam AI Examples

This directory contains comprehensive code examples for all Sarvam AI APIs.

## Prerequisites

1. Install the Sarvam AI Python SDK:
```bash
pip install sarvamai
```

2. Set up your API key:
```bash
export SARVAM_API_KEY="your_api_key_here"
```

Or create a `.env` file in the project root:
```
SARVAM_API_KEY=your_api_key_here
```

## Available Examples

### 1. Speech to Text (`speech_to_text.py`)
Demonstrates audio transcription in multiple Indian languages.

**Features:**
- Basic audio transcription
- Multi-language support (hi-IN, en-IN, ta-IN, te-IN, etc.)
- Model: saarika:v2.5

**Usage:**
```bash
python examples/speech_to_text.py
```

### 2. Speech to Text Translate (`speech_to_text_translate.py`)
Transcribes audio in Indian languages and translates to English.

**Features:**
- Automatic language detection
- Translation to English
- Batch processing support
- Model: saaras:v2.5

**Usage:**
```bash
python examples/speech_to_text_translate.py
```

### 3. Text to Speech (`text_to_speech.py`)
Converts text into natural-sounding speech in various Indian languages.

**Features:**
- Multiple language support
- Various voice speakers (meera, amit, arvind, anushka, etc.)
- Custom voice parameters (pitch, pace, loudness)
- Model: bulbul:v1

**Usage:**
```bash
python examples/text_to_speech.py
```

### 4. Text Translation (`text_translation.py`)
Translates text between Indian languages and English.

**Features:**
- Auto-detection of source language
- Translation between 10+ Indian languages
- Formal/informal translation modes
- Gender-based translation
- Model: mayura:v1

**Usage:**
```bash
python examples/text_translation.py
```

### 5. Chat Completion (`chat_completion.py`)
Conversational AI and text generation.

**Features:**
- Multi-turn conversations
- System prompts support
- Temperature and parameter tuning
- Available models: sarvam-2b, sarvam-m, sarvam-1

**Usage:**
```bash
python examples/chat_completion.py
```

### 6. End-to-End Example (`end_to_end_example.py`)
Complete workflow combining multiple APIs.

**Features:**
- Text translation workflow
- Text-to-speech conversion
- Speech transcription
- Chat-based analysis
- Multilingual chatbot example

**Usage:**
```bash
python examples/end_to_end_example.py
```

## Supported Languages

Sarvam AI supports the following Indian languages:

- **Hindi (hi-IN)**
- **English (en-IN)**
- **Bengali (bn-IN)**
- **Gujarati (gu-IN)**
- **Kannada (kn-IN)**
- **Malayalam (ml-IN)**
- **Marathi (mr-IN)**
- **Odia (or-IN)**
- **Punjabi (pa-IN)**
- **Tamil (ta-IN)**
- **Telugu (te-IN)**

## API Models

### Speech to Text
- **saarika:v2.5** - Latest transcription model

### Speech to Text Translate
- **saaras:v2.5** - Translation-enabled transcription

### Text to Speech
- **bulbul:v1** - Natural voice synthesis

### Text Translation
- **mayura:v1** - Neural machine translation

### Chat Completion
- **sarvam-2b** - Lightweight, fast responses
- **sarvam-m** - Balanced performance
- **sarvam-1** - Full-featured model

## Error Handling

All examples include proper error handling. Common errors:

1. **Missing API Key**: Set `SARVAM_API_KEY` environment variable
2. **File Not Found**: Provide valid audio file paths
3. **API Errors**: Check API quota and connectivity

## Additional Resources

- [Sarvam AI Documentation](https://docs.sarvam.ai)
- [API Reference](https://docs.sarvam.ai/api-reference-docs)
- [Dashboard](https://dashboard.sarvam.ai)
- [Discord Community](https://discord.com/invite/5rAsykttcs)

## Contributing

Feel free to add more examples or improve existing ones!
