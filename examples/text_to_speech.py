"""
Sarvam AI - Text to Speech
---------------------------
This example demonstrates how to use Sarvam AI's text-to-speech API
to convert text into natural-sounding speech in various Indian languages.

Available Models:
- bulbul:v2 (default) - 7 speakers, supports pitch/loudness/pace
- bulbul:v3-beta (new) - 31 speakers, supports temperature

bulbul:v2 Speakers (7): anushka, manisha, vidya, arya, abhilash, karun, hitesh
bulbul:v3-beta Speakers (31): Aditya (default), Ritu, Priya, Rohan, and 27 more

Supported languages: hi-IN, bn-IN, kn-IN, ml-IN, mr-IN, or-IN, pa-IN, ta-IN, te-IN, gu-IN, en-IN
"""

import os
import base64
from sarvamai import SarvamAI

def text_to_speech(
    text: str,
    target_language_code: str = "hi-IN",
    speaker: str = "anushka",
    pitch: float = 0.0,
    pace: float = 1.0,
    loudness: float = 1.5,
    speech_sample_rate: int = 8000,
    enable_preprocessing: bool = True,
    model: str = "bulbul:v2"
):
    """
    Convert text to speech using bulbul:v2.
    
    Args:
        text: The text to convert to speech
        target_language_code: Target language code (default: hi-IN)
        speaker: Voice speaker name (default: anushka)
                 v2 speakers: anushka, manisha, vidya, arya, abhilash, karun, hitesh
        pitch: Voice pitch adjustment (default: 0.0, range: -2.0 to 2.0)
        pace: Speaking pace (default: 1.0, range: 0.5 to 2.0)
        loudness: Audio loudness (default: 1.5, range: 0.5 to 3.0)
        speech_sample_rate: Audio sample rate in Hz (default: 8000)
        enable_preprocessing: Enable text preprocessing (default: True)
        model: TTS model version (default: bulbul:v2)
    
    Returns:
        Audio response with base64 encoded audio data
    """
    # Initialize the client with API key from environment
    client = SarvamAI(
        api_subscription_key=os.getenv("SARVAM_API_KEY"),
    )
    
    # Convert text to speech
    response = client.text_to_speech.convert(
        text=text,
        target_language_code=target_language_code,
        speaker=speaker,
        pitch=pitch,
        pace=pace,
        loudness=loudness,
        speech_sample_rate=speech_sample_rate,
        enable_preprocessing=enable_preprocessing,
        model=model
    )
    
    return response
def text_to_speech_v3(
    text: str,
    target_language_code: str = "hi-IN",
    speaker: str = "aditya",
    temperature: float = 1.0,
    speech_sample_rate: int = 8000,
    enable_preprocessing: bool = True,
    model: str = "bulbul:v3-beta"
):
    """
    Convert text to speech using bulbul:v3-beta.
    
    Args:
        text: The text to convert to speech
        target_language_code: Target language code (default: hi-IN)
        speaker: Voice speaker name (default: aditya)
                 v3-beta has 31 speakers including: aditya, ritu, priya, rohan, etc. (all lowercase)
        temperature: Controls randomness/expressiveness (default: 1.0, range: 0.0 to 2.0)
        speech_sample_rate: Audio sample rate in Hz (default: 8000)
        enable_preprocessing: Enable text preprocessing (default: True)
        model: TTS model version (default: bulbul:v3-beta)
    
    Returns:
        Audio response with base64 encoded audio data
    """
    # Initialize the client with API key from environment
    client = SarvamAI(
        api_subscription_key=os.getenv("SARVAM_API_KEY"),
    )
    
    # Convert text to speech with v3-beta parameters
    response = client.text_to_speech.convert(
        text=text,
        target_language_code=target_language_code,
        speaker=speaker,
        temperature=temperature,
        speech_sample_rate=speech_sample_rate,
        enable_preprocessing=enable_preprocessing,
        model=model
    )
    
    return response


def save_audio(audio_base64: str, output_path: str):
    """
    Save base64 encoded audio to a file.
    
    Args:
        audio_base64: Base64 encoded audio data
        output_path: Path to save the audio file
    """
    audio_data = base64.b64decode(audio_base64)
    with open(output_path, "wb") as f:
        f.write(audio_data)
    print(f"Audio saved to: {output_path}")


def main():
    """Example usage of text to speech API."""
    
    # Example 1: Basic text to speech with bulbul:v2
    print("=" * 50)
    print("Example 1: Basic Text to Speech (Hindi, bulbul:v2)")
    print("=" * 50)
    
    text = "नमस्ते, सर्वम एआई में आपका स्वागत है। यह एक टेक्स्ट टु स्पीच डेमो है।"
    
    try:
        result = text_to_speech(
            text=text,
            target_language_code="hi-IN",
            speaker="Anushka",
            model="bulbul:v2"
        )
        
        # Save the audio file
        save_audio(result.audios[0], "output_hindi_v2.wav")
        print(f"Generated audio duration: {result.duration} seconds")
        
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 2: Different speakers with bulbul:v2
    print("\n" + "=" * 50)
    print("Example 2: Multiple Speakers (bulbul:v2)")
    print("=" * 50)
    
    examples_v2 = [
        {
            "text": "Welcome to Sarvam AI!",
            "language": "en-IN",
            "speaker": "abhilash",  # Male voice
            "output": "output_english_v2.wav"
        },
        {
            "text": "வணக்கம், சர்வம் AI-க்கு வரவேற்கிறோம்",
            "language": "ta-IN",
            "speaker": "manisha",  # Female voice
            "output": "output_tamil_v2.wav"
        },
        {
            "text": "ಸ್ವಾಗತ ಸರ್ವಮ್ AI ಗೆ",
            "language": "kn-IN",
            "speaker": "vidya",  # Female voice
            "output": "output_kannada_v2.wav"
        }
    ]
    
    for example in examples_v2:
        print(f"\nGenerating speech in {example['language']} with speaker {example['speaker']}...")
        try:
            result = text_to_speech(
                text=example["text"],
                target_language_code=example["language"],
                speaker=example["speaker"],
                model="bulbul:v2"
            )
            save_audio(result.audios[0], example["output"])
        except Exception as e:
            print(f"Error: {e}")
    
    # Example 3: Custom voice parameters with bulbul:v2
    print("\n" + "=" * 50)
    print("Example 3: Custom Voice Parameters (bulbul:v2)")
    print("=" * 50)
    
    text = "यह एक कस्टम वॉयस पैरामीटर्स का डेमो है।"
    
    try:
        result = text_to_speech(
            text=text,
            target_language_code="hi-IN",
            speaker="karun",
            pitch=0.5,      # Slightly higher pitch
            pace=1.2,       # Faster pace
            loudness=2.0,   # Louder volume
            model="bulbul:v2"
        )
        save_audio(result.audios[0], "output_custom_v2.wav")
        
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 4: Using bulbul:v3-beta with new features
    print("\n" + "=" * 50)
    print("Example 4: bulbul:v3-beta with Temperature Control")
    print("=" * 50)
    
    text = "यह बुलबुल वर्जन 3 बीटा का डेमो है। इसमें 31 नए वॉइस हैं।"
    
    try:
        # More expressive/random (higher temperature)
        result = text_to_speech_v3(
            text=text,
            target_language_code="hi-IN",
            speaker="aditya",  # Default v3-beta speaker
            temperature=1.5,   # More expressive
            model="bulbul:v3-beta"
        )
        save_audio(result.audios[0], "output_v3_beta_expressive.wav")
        print("Generated with high temperature (more expressive)")
        
        # More consistent/deterministic (lower temperature)
        result = text_to_speech_v3(
            text=text,
            target_language_code="hi-IN",
            speaker="ritu",    # Another v3-beta speaker
            temperature=0.3,   # More consistent
            model="bulbul:v3-beta"
        )
        save_audio(result.audios[0], "output_v3_beta_consistent.wav")
        print("Generated with low temperature (more consistent)")
        
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 5: Comparing v2 and v3-beta
    print("\n" + "=" * 50)
    print("Example 5: Comparing bulbul:v2 vs bulbul:v3-beta")
    print("=" * 50)
    
    comparison_text = "Hello, this is a comparison between version 2 and version 3."
    
    try:
        # v2 version
        result_v2 = text_to_speech(
            text=comparison_text,
            target_language_code="en-IN",
            speaker="arya",
            model="bulbul:v2"
        )
        save_audio(result_v2.audios[0], "comparison_v2.wav")
        print("Generated with bulbul:v2 (speaker: Arya)")
        
        # v3-beta version
        result_v3 = text_to_speech_v3(
            text=comparison_text,
            target_language_code="en-IN",
            speaker="priya",
            model="bulbul:v3-beta"
        )
        save_audio(result_v3.audios[0], "comparison_v3_beta.wav")
        print("Generated with bulbul:v3-beta (speaker: Priya)")
        
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
