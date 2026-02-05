"""
Sarvam AI - Speech to Text Translate
-------------------------------------
This example demonstrates how to use Sarvam AI's speech-to-text-translate API
to transcribe audio in Indian languages and translate it to English.

Model: saaras:v2.5
Automatically detects the source language and translates to English
"""

import os
from sarvamai import SarvamAI

def transcribe_and_translate(file_path: str):
    """
    Transcribe audio and translate to English.
    
    Args:
        file_path: Path to the audio file
    
    Returns:
        Translation response object with both transcript and translation
    """
    # Initialize the client with API key from environment
    client = SarvamAI(
        api_subscription_key=os.getenv("SARVAM_API_KEY"),
    )
    
    # Transcribe and translate the audio file
    with open(file_path, "rb") as audio_file:
        response = client.speech_to_text.translate(
            file=audio_file,
            model="saaras:v2.5"
        )
    
    return response


def main():
    """Example usage of speech to text translate API."""
    
    # Example 1: Basic transcription and translation
    print("=" * 50)
    print("Example 1: Transcribe and Translate to English")
    print("=" * 50)
    
    audio_file = "hindi_audio.wav"  # Replace with your audio file
    
    try:
        result = transcribe_and_translate(audio_file)
        print(f"Original Transcript: {result.transcript}")
        print(f"English Translation: {result.translation}")
        print(f"Detected Language: {result.language_code}")
    except FileNotFoundError:
        print(f"Audio file '{audio_file}' not found. Please provide a valid audio file.")
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 2: Batch processing multiple files
    print("\n" + "=" * 50)
    print("Example 2: Batch Translation")
    print("=" * 50)
    
    audio_files = [
        "hindi_sample.wav",
        "tamil_sample.wav",
        "bengali_sample.wav"
    ]
    
    for audio_file in audio_files:
        print(f"\nProcessing: {audio_file}")
        # Uncomment to use actual files
        # result = transcribe_and_translate(audio_file)
        # print(f"Translation: {result.translation}")


if __name__ == "__main__":
    main()
