# Sarvam AI Skills - Repository Structure

## File Tree

```
sarvam-skills/
├── .env                          # Environment variables (API key)
├── .env.example                  # Environment template
├── requirements.txt              # Python dependencies
├── README.md                     # Main documentation
├── SKILL.md                      # Skill definition (this file)
├── CONTRIBUTING.md               # Contribution guidelines
│
├── examples/                     # Working code examples
│   ├── speech_to_text.py         # STT: Transcribe audio to text
│   ├── speech_to_text_translate.py  # STT-Translate: Transcribe + translate
│   ├── text_to_speech.py         # TTS: Generate speech from text
│   ├── text_translation.py       # Translation: Text translation
│   ├── chat_completion.py        # Chat: Conversational AI
│   ├── document_intelligence.py  # Document: PDF/image text extraction
│   ├── end_to_end_example.py     # Complete multi-API workflows
│   └── README.md                 # Examples documentation
│
└── templates/                    # Skill templates & guides
    ├── speech-to-text-template.md        # STT skill template
    ├── text-to-speech-template.md        # TTS skill template
    ├── text-translation-template.md      # Translation template
    ├── chat-completion-template.md       # Chat skill template
    ├── document-intelligence-template.md # Document processing template
    ├── skill-template.md                 # General skill template
    └── README.md                         # Templates overview
```

## File Details & Use Cases

### Configuration Files (Root)

| File | Size | Use Case | Contents |
|------|------|----------|----------|
| `.env` | ~51B | **Your API key storage** | `SARVAM_API_KEY=your_key` - Already configured |
| `.env.example` | ~15B | Template for new users | Shows required environment variables |
| `requirements.txt` | ~37B | Python dependencies | `sarvamai`, `python-dotenv` |
| `README.md` | ~9.7KB | Main documentation | Project overview, all APIs explained |
| `SKILL.md` | This file | Skill definition | Anthropic-format skill file |
| `CONTRIBUTING.md` | ~3.6KB | Contribution guide | How to add examples/templates |

### Examples Directory (`examples/`)

Working Python scripts demonstrating each API:

**speech_to_text.py** (~2.2KB)
- **Use Case**: Audio transcription in 11 Indian languages
- **API**: Speech-to-Text (saarika:v2.5)
- **Shows**: File upload, language selection, error handling
- **Run**: `python examples/speech_to_text.py`

**speech_to_text_translate.py** (~2.2KB)
- **Use Case**: Transcribe audio and auto-translate to English
- **API**: Speech-to-Text-Translate (saaras:v2.5)
- **Shows**: Auto-detection, translation workflows, batch processing
- **Run**: `python examples/speech_to_text_translate.py`

**text_to_speech.py** (~4.9KB)
- **Use Case**: Convert text to natural speech with voice customization
- **API**: Text-to-Speech (bulbul:v1)
- **Shows**: Multiple speakers, pitch/pace/loudness control, base64 audio handling
- **Run**: `python examples/text_to_speech.py`

**text_translation.py** (~4.7KB)
- **Use Case**: Translate text between Indian languages
- **API**: Text Translation (mayura:v1)
- **Shows**: Auto-detection, formal/informal modes, gender-aware translation
- **Run**: `python examples/text_translation.py`

**chat_completion.py** (~5.5KB)
- **Use Case**: Conversational AI and text generation
- **API**: Chat Completion (sarvam-2b/m/1)
- **Shows**: Multi-turn conversations, model selection, temperature tuning
- **Run**: `python examples/chat_completion.py`

**document_intelligence.py** (~5.8KB)
- **Use Case**: Extract text from PDFs and images in 23 languages
- **API**: Document Intelligence (sarvam-vision)
- **Shows**: Job-based workflow, file upload, polling, output download
- **Run**: `python examples/document_intelligence.py`

**end_to_end_example.py** (~6.4KB)
- **Use Case**: Complete workflows combining multiple APIs
- **APIs**: All 5 APIs combined
- **Shows**: Multilingual chatbot, voice assistant, content localization
- **Run**: `python examples/end_to_end_example.py`

**README.md** (~3.5KB)
- Use Case: Documentation for all examples
- Contents: Prerequisites, usage, language support, troubleshooting

### Templates Directory (`templates/`)

Comprehensive guides for building skills:

**speech-to-text-template.md** (~3.2KB)
- **Use Case**: Guide for creating STT-based skills
- **Contents**: API docs, parameters, Python/cURL examples, best practices

**text-to-speech-template.md** (~5.1KB)
- **Use Case**: Guide for creating TTS-based skills
- **Contents**: Voice customization, speakers, audio generation patterns

**text-translation-template.md** (~6.6KB)
- **Use Case**: Guide for creating translation skills
- **Contents**: Auto-detection, modes, gender context, batch processing

**chat-completion-template.md** (~9.2KB)
- **Use Case**: Guide for creating chat AI skills
- **Contents**: Model selection, conversation management, streaming

**document-intelligence-template.md** (~7.8KB)
- **Use Case**: Guide for creating document processing skills
- **Contents**: Job workflow, format selection, batch processing

**skill-template.md** (~227B)
- **Use Case**: Template for any new skill
- **Contents**: Basic structure, placeholders

**README.md** (~6.0KB)
- **Use Case**: Overview of all templates
- **Contents**: When to use each template, quick start

## Quick Usage Guide

### Installation
```bash
pip install -r requirements.txt
# API key already configured in .env
```

### Run Examples
```bash
# Speech to Text
python examples/speech_to_text.py

# Text to Speech
python examples/text_to_speech.py

# Translation
python examples/text_translation.py

# Chat
python examples/chat_completion.py

# Document Intelligence
python examples/document_intelligence.py

# Complete workflow
python examples/end_to_end_example.py
```

### Use Templates
1. Choose template from `templates/` directory
2. Follow the guide for your specific API
3. Reference code examples from `examples/`

## API Models Reference

| API | Model | File | Template |
|-----|-------|------|----------|
| Speech-to-Text | saarika:v2.5 | `examples/speech_to_text.py` | `templates/speech-to-text-template.md` |
| STT-Translate | saaras:v2.5 | `examples/speech_to_text_translate.py` | - |
| Text-to-Speech | bulbul:v1 | `examples/text_to_speech.py` | `templates/text-to-speech-template.md` |
| Translation | mayura:v1 | `examples/text_translation.py` | `templates/text-translation-template.md` |
| Chat | sarvam-2b/m/1 | `examples/chat_completion.py` | `templates/chat-completion-template.md` |
| Document Intelligence | sarvam-vision | `examples/document_intelligence.py` | `templates/document-intelligence-template.md` |

## Supported Languages

**Core 11 languages** (STT, TTS, Translation): hi-IN (Hindi), en-IN (English), bn-IN (Bengali), gu-IN (Gujarati), kn-IN (Kannada), ml-IN (Malayalam), mr-IN (Marathi), or-IN (Odia), pa-IN (Punjabi), ta-IN (Tamil), te-IN (Telugu)

**Extended 22 languages** (Translation): + as-IN, brx-IN, doi-IN, kok-IN, ks-IN, mai-IN, mni-IN, ne-IN, sa-IN, sat-IN, sd-IN, ur-IN

**Document Intelligence 23 languages**: All 22 Indian languages + en-IN

## Total Files: 18

- **7 Python examples** in `examples/`
- **6 Markdown templates** in `templates/`
- **3 Configuration files** (`.env`, `.env.example`, `requirements.txt`)
- **2 Documentation files** (`README.md`, `CONTRIBUTING.md`)
- **1 Skill file** (`SKILL.md`)

## External Resources

- Documentation: https://docs.sarvam.ai
- Dashboard: https://dashboard.sarvam.ai
- Discord: https://discord.com/invite/5rAsykttcs
- Python SDK: https://pypi.org/project/sarvamai/