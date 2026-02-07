"""
Sarvam AI - Text to Speech
---------------------------
This example demonstrates how to use Sarvam AI's text-to-speech API
to convert text into natural-sounding speech in various Indian languages.

Available Model:
- bulbul:v3 (default) - 45 speakers, supports pace/temperature

bulbul:v3 Speakers (45): aditya (default), shubh, ritu, priya, neha, rahul, pooja, rohan, simran, kavya, amit, dev, ishita, shreya, ratan, varun, manan, sumit, roopa, kabir, aayan, ashutosh, advait, amelia, sophia, anand, tanya, tarun, sunny, mani, gokul, vijay, shruti, suhani, mohit, kavitha, rehan, soham, rupali, anushka, abhilash, manisha, vidya, arya, karun, hitesh

Supported languages: hi-IN, bn-IN, kn-IN, ml-IN, mr-IN, or-IN, pa-IN, ta-IN, te-IN, gu-IN, en-IN
"""

import os
import base64
from sarvamai import SarvamAI

def text_to_speech(
    text: str,
    target_language_code: str = "hi-IN",
    speaker: str = "aditya",
    pace: float = 1.0,
    temperature: float = 0.6,
    speech_sample_rate: int = 24000,
    model: str = "bulbul:v3"
):
    """
    Convert text to speech using bulbul:v3.
    
    Args:
        text: The text to convert to speech
        target_language_code: Target language code (default: hi-IN)
        speaker: Voice speaker name (default: aditya)
                 v3 speakers: aditya (default), shubh, ritu, priya, neha, rahul, pooja,
                 rohan, simran, kavya, amit, dev, ishita, shreya, ratan, varun, manan,
                 sumit, roopa, kabir, aayan, ashutosh, advait, amelia, sophia, anand,
                 tanya, tarun, sunny, mani, gokul, vijay, shruti, suhani, mohit, kavitha,
                 rehan, soham, rupali, anushka, abhilash, manisha, vidya, arya, karun, hitesh
        pace: Speaking pace (default: 1.0, range: 0.5 to 2.0)
        temperature: Controls randomness/expressiveness (default: 0.6, range: 0.01 to 2.0)
        speech_sample_rate: Audio sample rate in Hz (default: 24000)
        model: TTS model version (default: bulbul:v3)
    
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
        pace=pace,
        temperature=temperature,
        speech_sample_rate=speech_sample_rate,
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
    
    # Example 1: Basic text to speech with bulbul:v3
    print("=" * 50)
    print("Example 1: Basic Text to Speech (Hindi, bulbul:v3)")
    print("=" * 50)
    
    text = "नमस्ते, सर्वम एआई में आपका स्वागत है। यह एक टेक्स्ट टु स्पीच डेमो है।"
    
    try:
        result = text_to_speech(
            text=text,
            target_language_code="hi-IN",
            speaker="shubh",
            model="bulbul:v3"
        )
        
        # Save the audio file
        save_audio(result.audios[0], "output_hindi_v3.wav")
        
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 2: Different speakers with bulbul:v3
    print("\n" + "=" * 50)
    print("Example 2: Multiple Speakers (bulbul:v3)")
    print("=" * 50)
    
    examples_v3 = [
        {
            "text": "Welcome to Sarvam AI!",
            "language": "en-IN",
            "speaker": "aditya",  # Default male voice
            "output": "output_english_v3.wav"
        },
        {
            "text": "வணக்கம், சர்வம் AI-க்கு வரவேற்கிறோம்",
            "language": "ta-IN",
            "speaker": "ritu",  # Female voice
            "output": "output_tamil_v3.wav"
        },
        {
            "text": "ಸ್ವಾಗತ ಸರ್ವಮ್ AI ಗೆ",
            "language": "kn-IN",
            "speaker": "priya",  # Female voice
            "output": "output_kannada_v3.wav"
        }
    ]
    
    for example in examples_v3:
        print(f"\nGenerating speech in {example['language']} with speaker {example['speaker']}...")
        try:
            result = text_to_speech(
                text=example["text"],
                target_language_code=example["language"],
                speaker=example["speaker"],
                model="bulbul:v3"
            )
            save_audio(result.audios[0], example["output"])
        except Exception as e:
            print(f"Error: {e}")
    
    # Example 3: Custom parameters with bulbul:v3
    print("\n" + "=" * 50)
    print("Example 3: Custom Parameters (bulbul:v3)")
    print("=" * 50)
    
    text = "यह बुलबुल वर्जन 3 का डेमो है। इसमें 45 से अधिक वॉइस हैं।"
    
    try:
        result = text_to_speech(
            text=text,
            target_language_code="hi-IN",
            speaker="neha",
            pace=1.2,         # Faster pace
            temperature=0.7,  # More expressive
            model="bulbul:v3"
        )
        save_audio(result.audios[0], "output_custom_v3.wav")
        
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
