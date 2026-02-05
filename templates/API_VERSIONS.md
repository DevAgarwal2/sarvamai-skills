# Sarvam AI API Versions - Cross-Verified

**Last Verified:** February 1, 2026  
**Source:** Official Sarvam AI Documentation

## API Endpoints & Current Versions

### 1. Speech-to-Text
**Endpoint:** `https://api.sarvam.ai/speech-to-text`

| Model | Version | Status | Default | Notes |
|-------|---------|--------|---------|-------|
| saarika | v2.5 | ✅ Active | Yes | Standard transcription, 11 languages |
| saaras | v3 | ✅ Active | No | Advanced with 5 modes (transcribe, translate, verbatim, translit, codemix) |

**Supported Languages:** hi-IN, bn-IN, kn-IN, ml-IN, mr-IN, od-IN, pa-IN, ta-IN, te-IN, en-IN, gu-IN

---

### 2. Speech-to-Text-Translate
**Endpoint:** `https://api.sarvam.ai/speech-to-text-translate`

| Model | Version | Status | Default |
|-------|---------|--------|---------|
| saaras | v2.5 | ✅ Active | Yes |

**Function:** Transcribes audio in any Indian language and translates to English

---

### 3. Text-to-Speech  
**Endpoint:** `https://api.sarvam.ai/text-to-speech`

| Model | Version | Status | Default | Max Chars |
|-------|---------|--------|---------|-----------|
| bulbul | v2 | ✅ Active | Yes | 1500 |
| bulbul | v3-beta | ✅ Active | No | 2500 |

**bulbul:v2 Speakers (7 total):**
- Female: Anushka (default), Manisha, Vidya, Arya
- Male: Abhilash, Karun, Hitesh

**bulbul:v3-beta Speakers (31 total):**
- Default: Aditya
- All: Aditya, Ritu, Priya, Neha, Rahul, Pooja, Rohan, Simran, Kavya, Amit, Dev, Ishita, Shreya, Ratan, Varun, Manan, Sumit, Roopa, Kabir, Aayan, Shubh, Ashutosh, Advait, Amelia, Sophia

**Parameter Differences:**

| Parameter | bulbul:v2 | bulbul:v3-beta |
|-----------|-----------|----------------|
| pitch | ✅ Supported (-0.75 to 0.75) | ❌ NOT supported |
| pace | ✅ (0.3 to 3.0) | ✅ (0.5 to 2.0) |
| loudness | ✅ (0.3 to 3.0) | ❌ NOT supported |
| temperature | ❌ Not available | ✅ (0.01 to 1.0, default 0.6) |
| preprocessing | Optional (default false) | ✅ Always enabled |
| sample_rate | Default 22050 Hz | Default 24000 Hz |

**Supported Languages:** bn-IN, en-IN, gu-IN, hi-IN, kn-IN, ml-IN, mr-IN, od-IN, pa-IN, ta-IN, te-IN

---

### 4. Text Translation
**Endpoint:** `https://api.sarvam.ai/translate`

| Model | Version | Status | Languages | Max Chars |
|-------|---------|--------|-----------|-----------|
| mayura | v1 | ✅ Active | 11 | 1000 |
| sarvam-translate | v1 | ✅ Active | 22 | 2000 |

**mayura:v1 Languages (11):**
Bengali, English, Gujarati, Hindi, Kannada, Malayalam, Marathi, Odia, Punjabi, Tamil, Telugu

**sarvam-translate:v1 Languages (22 - ALL 11 + these):**
Assamese (as-IN), Bodo (brx-IN), Dogri (doi-IN), Konkani (kok-IN), Kashmiri (ks-IN), Maithili (mai-IN), Manipuri (mni-IN), Nepali (ne-IN), Sanskrit (sa-IN), Santali (sat-IN), Sindhi (sd-IN), Urdu (ur-IN)

**Translation Modes:**

| Mode | mayura:v1 | sarvam-translate:v1 |
|------|-----------|---------------------|
| formal | ✅ | ✅ |
| modern-colloquial | ✅ | ❌ |
| classic-colloquial | ✅ | ❌ |
| code-mixed | ✅ | ❌ |

**Additional Features (mayura:v1 only):**
- Auto language detection (source_language_code: "auto")
- Output script control (roman, fully-native, spoken-form-in-native)
- Numerals format (international/native)

---

### 5. Chat Completion
**Endpoint:** `https://api.sarvam.ai/v1/chat/completions`

| Model | Status | Parameters |
|-------|--------|------------|
| sarvam-m | ✅ Active ONLY | 24B parameters, multilingual |
| sarvam-2b | ❌ NOT in API docs | Not available |
| sarvam-1 | ❌ NOT in API docs | Not available |

**Supported Parameters:**
- temperature (0-2, default 0.2)
- top_p (0-1, default 1)
- max_tokens
- stream (true/false)
- reasoning_effort (low/medium/high)
- wiki_grounding (true/false)
- frequency_penalty (-2 to 2)
- presence_penalty (-2 to 2)
- seed (for deterministic outputs)
- n (number of completions)
- stop (stop sequences)

---

## Breaking Changes from Our Examples

### ❌ What Was WRONG in Our Examples:

1. **Text-to-Speech Speakers**
   - Listed: meera, amol, arvind
   - **Reality:** Anushka, Abhilash, Karun, Manisha, Vidya, Arya, Hitesh (v2) or 31 speakers (v3-beta)

2. **Chat Models**
   - Listed: sarvam-2b, sarvam-m, sarvam-1
   - **Reality:** ONLY sarvam-m is available

3. **Translation Languages**
   - Listed: 11 languages
   - **Reality:** 22 languages with sarvam-translate:v1

4. **STT Models**
   - Missed: saaras:v3 with 5 modes
   - Only mentioned: saarika:v2.5

5. **Model Versions**
   - Listed: bulbul:v1
   - **Reality:** bulbul:v2 (current default), bulbul:v3-beta (new)

---

## Recommended Updates

### High Priority
1. ✅ Update TTS examples with correct speakers
2. ✅ Update chat examples to ONLY use sarvam-m
3. ✅ Add version markers to ALL examples
4. ✅ Document bulbul:v2 vs v3-beta differences

### Medium Priority
1. Add sarvam-translate:v1 examples (22 languages)
2. Add saaras:v3 examples with 5 modes
3. Add TypeScript examples
4. Create CLI tool

### Low Priority
1. Add streaming examples
2. Add batch API examples
3. Add WebSocket examples

---

## Version History

| Date | API | Change |
|------|-----|--------|
| 2026-02-01 | All | Cross-verified all endpoints |
| Unknown | TTS | bulbul:v3-beta released |
| Unknown | Translation | sarvam-translate:v1 with 22 languages |
| Unknown | STT | saaras:v3 with 5 modes |

---

## Authentication

All endpoints use: `api-subscription-key` header
- STT/TTS/Translation: Header directly
- Chat: Bearer token in Authorization header (but SDK handles this)

---

## Official Documentation
https://docs.sarvam.ai/api-reference-docs/introduction
