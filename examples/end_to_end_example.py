"""
Sarvam AI - End-to-End Example
-------------------------------
This example demonstrates a complete workflow using multiple Sarvam AI APIs:
1. Translate text from English to Hindi
2. Convert translated text to speech
3. Transcribe the generated speech back to text
4. Use chat completion for analysis

This showcases how different APIs can work together.
"""

import os
import base64
from sarvamai import SarvamAI

def end_to_end_workflow():
    """
    Demonstrates a complete workflow using multiple Sarvam AI APIs.
    """
    # Initialize the client
    client = SarvamAI(
        api_subscription_key=os.getenv("SARVAM_API_KEY")
    )
    
    print("=" * 60)
    print("Sarvam AI - End-to-End Workflow Demo")
    print("=" * 60)
    
    # Step 1: Text Translation
    print("\n[Step 1] Translating English text to Hindi...")
    original_text = "Welcome to Sarvam AI. This is an amazing platform for Indian language AI."
    
    try:
        translation_response = client.text.translate(
            input=original_text,
            source_language_code="en-IN",
            target_language_code="hi-IN",
            speaker_gender="Male"
        )
        translated_text = translation_response.translated_text
        
        print(f"Original (English): {original_text}")
        print(f"Translated (Hindi): {translated_text}")
        
    except Exception as e:
        print(f"Translation Error: {e}")
        return
    
    # Step 2: Text to Speech
    print("\n[Step 2] Converting translated text to speech...")
    
    try:
        tts_response = client.text_to_speech.convert(
            text=translated_text,
            target_language_code="hi-IN",
            speaker="meera"
        )
        
        # Save the generated audio
        audio_data = base64.b64decode(tts_response.audios[0])
        audio_file = "workflow_audio.wav"
        with open(audio_file, "wb") as f:
            f.write(audio_data)
        
        print(f"Generated audio saved to: {audio_file}")
        print(f"Duration: {tts_response.duration} seconds")
        
    except Exception as e:
        print(f"Text-to-Speech Error: {e}")
        return
    
    # Step 3: Speech to Text (Transcription)
    print("\n[Step 3] Transcribing the generated speech...")
    
    try:
        with open(audio_file, "rb") as f:
            stt_response = client.speech_to_text.transcribe(
                file=f,
                model="saarika:v2.5",
                language_code="hi-IN"
            )
        
        transcribed_text = stt_response.transcript
        print(f"Transcribed text: {transcribed_text}")
        
        # Compare original translation with transcription
        print("\nComparison:")
        print(f"Original translation: {translated_text}")
        print(f"Transcribed text:     {transcribed_text}")
        
    except Exception as e:
        print(f"Speech-to-Text Error: {e}")
        return
    
    # Step 4: Chat Completion for Analysis
    print("\n[Step 4] Using chat completion to analyze the workflow...")
    
    try:
        analysis_prompt = f"""
        I performed the following AI workflow:
        1. Translated: "{original_text}" from English to Hindi
        2. Got: "{translated_text}"
        3. Converted it to speech
        4. Transcribed back: "{transcribed_text}"
        
        Please analyze if the translation and transcription are accurate and provide feedback.
        """
        
        chat_response = client.chat.completions(
            messages=[
                {"role": "user", "content": analysis_prompt}
            ],
            model="sarvam-m",
            temperature=0.5
        )
        
        analysis = chat_response.choices[0].message.content
        print(f"AI Analysis:\n{analysis}")
        
    except Exception as e:
        print(f"Chat Completion Error: {e}")
        return
    
    print("\n" + "=" * 60)
    print("Workflow completed successfully!")
    print("=" * 60)


def multilingual_chatbot_example():
    """
    Example of building a multilingual chatbot using Sarvam AI.
    """
    print("\n\n" + "=" * 60)
    print("Multilingual Chatbot Example")
    print("=" * 60)
    
    client = SarvamAI(
        api_subscription_key=os.getenv("SARVAM_API_KEY")
    )
    
    # Simulate user input in Hindi
    user_input_hindi = "भारत की राजधानी क्या है?"
    print(f"\nUser (Hindi): {user_input_hindi}")
    
    # Step 1: Translate to English for processing
    try:
        translation = client.text.translate(
            input=user_input_hindi,
            source_language_code="hi-IN",
            target_language_code="en-IN"
        )
        user_input_english = translation.translated_text
        print(f"Translated to English: {user_input_english}")
        
    except Exception as e:
        print(f"Translation Error: {e}")
        return
    
    # Step 2: Get response using chat completion
    try:
        chat_response = client.chat.completions(
            messages=[
                {"role": "user", "content": user_input_english}
            ],
            model="sarvam-2b"
        )
        bot_response_english = chat_response.choices[0].message.content
        print(f"\nBot Response (English): {bot_response_english}")
        
    except Exception as e:
        print(f"Chat Error: {e}")
        return
    
    # Step 3: Translate response back to Hindi
    try:
        response_translation = client.text.translate(
            input=bot_response_english,
            source_language_code="en-IN",
            target_language_code="hi-IN"
        )
        bot_response_hindi = response_translation.translated_text
        print(f"Bot Response (Hindi): {bot_response_hindi}")
        
    except Exception as e:
        print(f"Translation Error: {e}")
        return
    
    # Step 4: Convert to speech
    try:
        tts_response = client.text_to_speech.convert(
            text=bot_response_hindi,
            target_language_code="hi-IN",
            speaker="arvind"
        )
        
        audio_data = base64.b64decode(tts_response.audios[0])
        with open("chatbot_response.wav", "wb") as f:
            f.write(audio_data)
        
        print("Audio response saved to: chatbot_response.wav")
        
    except Exception as e:
        print(f"TTS Error: {e}")
        return


def main():
    """Run all examples."""
    
    # Example 1: End-to-end workflow
    end_to_end_workflow()
    
    # Example 2: Multilingual chatbot
    multilingual_chatbot_example()


if __name__ == "__main__":
    main()
