"""
Sarvam AI - Speech to Text (Transcription)
-------------------------------------------
This example demonstrates how to use Sarvam AI's speech-to-text API
to transcribe audio files in various Indian languages.

Available Models:
- saarika:v2.5 - Standard transcription
- saaras:v3 - Advanced with 5 modes (transcribe, translate, verbatim, translit, codemix)

Supported languages: hi-IN, en-IN, bn-IN, gu-IN, kn-IN, ml-IN, mr-IN, or-IN, pa-IN, ta-IN, te-IN
"""

import os
from sarvamai import SarvamAI

def transcribe_audio(
    file_path: str, 
    language_code: str = "en-IN",
    model: str = "saarika:v2.5"
):
    """
    Transcribe an audio file to text using saarika:v2.5.
    
    Args:
        file_path: Path to the audio file (WAV, MP3, etc.)
        language_code: Language code (default: en-IN)
        model: Model to use (default: saarika:v2.5)
    
    Returns:
        Transcription response object
    """
    # Initialize the client with API key from environment
    client = SarvamAI(
        api_subscription_key=os.getenv("SARVAM_API_KEY"),
    )
    
    # Transcribe the audio file
    with open(file_path, "rb") as audio_file:
        response = client.speech_to_text.transcribe(
            file=audio_file,
            model=model,
            language_code=language_code
        )
    
    return response


def transcribe_with_mode(
    file_path: str,
    language_code: str = "en-IN",
    mode: str = "transcribe",
    model: str = "saaras:v3"
):
    """
    Transcribe audio using saaras:v3 with specific mode.
    
    Args:
        file_path: Path to the audio file
        language_code: Language code (default: en-IN)
        mode: Transcription mode - one of:
            - transcribe: Clean transcript (default)
            - translate: Translate to English
            - verbatim: Include all filler words
            - translit: Transliterate to Roman script
            - codemix: Handle code-mixed speech
        model: Model to use (default: saaras:v3)
    
    Returns:
        Transcription response object
    """
    # Initialize the client
    client = SarvamAI(
        api_subscription_key=os.getenv("SARVAM_API_KEY"),
    )
    
    # Transcribe with mode
    with open(file_path, "rb") as audio_file:
        response = client.speech_to_text.transcribe(
            file=audio_file,
            model=model,
            language_code=language_code,
            mode=mode
        )
    
    return response


def main():
    """Example usage of speech to text API."""
    
    # Example 1: Basic transcription with saarika:v2.5
    print("=" * 50)
    print("Example 1: Basic Audio Transcription (saarika:v2.5)")
    print("=" * 50)
    
    audio_file = "sample_audio.wav"  # Replace with your audio file path
    
    try:
        result = transcribe_audio(
            audio_file, 
            language_code="hi-IN",
            model="saarika:v2.5"
        )
        print(f"Transcription: {result.transcript}")
        print(f"Language: {result.language_code}")
    except FileNotFoundError:
        print(f"Audio file '{audio_file}' not found. Please provide a valid audio file.")
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 2: Using saaras:v3 with different modes
    print("\n" + "=" * 50)
    print("Example 2: saaras:v3 - All 5 Modes")
    print("=" * 50)
    
    audio_file = "sample_hindi.wav"  # Replace with your audio file
    
    modes = [
        ("transcribe", "Clean transcript (filler words removed)"),
        ("translate", "Transcribe + Translate to English"),
        ("verbatim", "Word-for-word including fillers"),
        ("translit", "Transliterated to Roman script"),
        ("codemix", "Code-mixed transcript (e.g., Hinglish)")
    ]
    
    print(f"\nProcessing audio file: {audio_file}")
    print(f"Language: hi-IN\n")
    
    for mode, description in modes:
        print(f"\n{mode.upper()} MODE:")
        print(f"Description: {description}")
        try:
            result = transcribe_with_mode(
                audio_file,
                language_code="hi-IN",
                mode=mode,
                model="saaras:v3"
            )
            print(f"Result: {result.transcript}")
        except FileNotFoundError:
            print(f"Audio file not found. Skipping {mode} mode demo.")
        except Exception as e:
            print(f"Error: {e}")
    
    # Example 3: Comparing saarika:v2.5 vs saaras:v3
    print("\n" + "=" * 50)
    print("Example 3: Model Comparison (saarika:v2.5 vs saaras:v3)")
    print("=" * 50)
    
    audio_file = "sample_audio.wav"
    
    try:
        # Standard transcription
        result_v2 = transcribe_audio(
            audio_file,
            language_code="en-IN",
            model="saarika:v2.5"
        )
        
        # Advanced transcription
        result_v3 = transcribe_with_mode(
            audio_file,
            language_code="en-IN",
            mode="transcribe",
            model="saaras:v3"
        )
        
        print("saarika:v2.5 (standard):")
        print(f"  {result_v2.transcript}")
        print("\nsaaras:v3 (advanced, clean mode):")
        print(f"  {result_v3.transcript}")
        
    except FileNotFoundError:
        print("Audio file not found. Please provide a valid audio file.")
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 4: Multi-language support
    print("\n" + "=" * 50)
    print("Example 4: Multi-language Support")
    print("=" * 50)
    
    languages = [
        ("en-IN", "English"),
        ("hi-IN", "Hindi"),
        ("ta-IN", "Tamil"),
        ("te-IN", "Telugu"),
        ("bn-IN", "Bengali")
    ]
    
    for lang_code, lang_name in languages:
        print(f"\nTranscribing in {lang_name} ({lang_code})...")
        # Uncomment and use actual audio files
        # try:
        #     result = transcribe_with_mode(
        #         f"audio_{lang_code}.wav",
        #         language_code=lang_code,
        #         mode="transcribe",
        #         model="saaras:v3"
        #     )
        #     print(f"Result: {result.transcript}")
        # except Exception as e:
        #     print(f"Error: {e}")
        print("(Skipped - audio file not available)")
    
    # Example 5: Use case scenarios
    print("\n" + "=" * 50)
    print("Example 5: Use Case Scenarios")
    print("=" * 50)
    
    use_cases = [
        {
            "name": "Legal Transcription",
            "mode": "verbatim",
            "description": "Captures every word including 'um', 'uh' for court records"
        },
        {
            "name": "International Communication",
            "mode": "translate",
            "description": "Transcribe regional language and translate to English"
        },
        {
            "name": "SMS/Chat Apps",
            "mode": "translit",
            "description": "Roman script for users without native keyboards"
        },
        {
            "name": "Urban Conversations",
            "mode": "codemix",
            "description": "Handles Hinglish and other code-mixed speech"
        },
        {
            "name": "Professional Documentation",
            "mode": "transcribe",
            "description": "Clean transcript for reports and documentation"
        }
    ]
    
    print("\nRecommended modes for different use cases:\n")
    for uc in use_cases:
        print(f"{uc['name']}:")
        print(f"  Mode: {uc['mode']}")
        print(f"  Description: {uc['description']}\n")


if __name__ == "__main__":
    main()
