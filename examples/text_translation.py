"""
Sarvam AI - Text Translation
-----------------------------
This example demonstrates how to use Sarvam AI's translation API
to translate text between various Indian languages.

Available Models:
- mayura:v1 - Supports 11 languages
- sarvam-translate:v1 - Supports 22 languages (recommended)

Auto-detection of source language available
"""

import os
from sarvamai import SarvamAI

def translate_text(
    text: str,
    source_language_code: str = "auto",
    target_language_code: str = "hi-IN",
    speaker_gender: str = "Male",
    mode: str = "formal",
    model: str = "sarvam-translate:v1",
    enable_preprocessing: bool = False
):
    """
    Translate text between languages.
    
    Args:
        text: The text to translate
        source_language_code: Source language code (default: auto)
        target_language_code: Target language code
        speaker_gender: Gender for translation context (Male/Female)
        mode: Translation formality mode (formal/informal)
        model: Translation model (mayura:v1 or sarvam-translate:v1 - recommended)
        enable_preprocessing: Enable text preprocessing
    
    Returns:
        Translation response object
    """
    # Initialize the client with API key from environment
    client = SarvamAI(
        api_subscription_key=os.getenv("SARVAM_API_KEY"),
    )
    
    # Translate the text
    response = client.text.translate(
        input=text,
        source_language_code=source_language_code,
        target_language_code=target_language_code,
        speaker_gender=speaker_gender,
        mode=mode,
        model=model,
        enable_preprocessing=enable_preprocessing
    )
    
    return response


def main():
    """Example usage of text translation API."""
    
    # Example 1: Basic translation with auto-detect using sarvam-translate:v1
    print("=" * 50)
    print("Example 1: Auto-detect and Translate (sarvam-translate:v1)")
    print("=" * 50)
    
    text = "Hello, how are you?"
    
    try:
        result = translate_text(
            text=text,
            source_language_code="auto",
            target_language_code="hi-IN",
            model="sarvam-translate:v1"
        )
        print(f"Original: {text}")
        print(f"Translated (Hindi): {result.translated_text}")
        
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 2: Using all 22 languages (sarvam-translate:v1)
    print("\n" + "=" * 50)
    print("Example 2: Translate to All 22 Languages (sarvam-translate:v1)")
    print("=" * 50)
    
    source_text = "Welcome to Sarvam AI"
    target_languages = {
        # Original 11 languages
        "hi-IN": "Hindi",
        "bn-IN": "Bengali",
        "gu-IN": "Gujarati",
        "kn-IN": "Kannada",
        "ml-IN": "Malayalam",
        "mr-IN": "Marathi",
        "or-IN": "Odia",
        "pa-IN": "Punjabi",
        "ta-IN": "Tamil",
        "te-IN": "Telugu",
        "en-IN": "English",
        # Additional 11 languages (only in sarvam-translate:v1)
        "as-IN": "Assamese",
        "brx-IN": "Bodo",
        "doi-IN": "Dogri",
        "gom-IN": "Konkani",
        "ks-IN": "Kashmiri",
        "mai-IN": "Maithili",
        "mni-IN": "Manipuri",
        "ne-IN": "Nepali",
        "sa-IN": "Sanskrit",
        "sat-IN": "Santali",
        "sd-IN": "Sindhi",
        "ur-IN": "Urdu"
    }
    
    print(f"Source text: {source_text}\n")
    
    for lang_code, lang_name in target_languages.items():
        try:
            result = translate_text(
                text=source_text,
                source_language_code="en-IN",
                target_language_code=lang_code,
                model="sarvam-translate:v1"
            )
            print(f"{lang_name:12} ({lang_code:8}): {result.translated_text}")
        except Exception as e:
            print(f"{lang_name:12} ({lang_code:8}): Error - {e}")
    
    # Example 3: Comparing mayura:v1 vs sarvam-translate:v1
    print("\n" + "=" * 50)
    print("Example 3: Model Comparison (mayura:v1 vs sarvam-translate:v1)")
    print("=" * 50)
    
    text = "Good morning, have a great day!"
    
    try:
        # Using mayura:v1
        result_v1 = translate_text(
            text=text,
            source_language_code="en-IN",
            target_language_code="hi-IN",
            model="mayura:v1"
        )
        
        # Using sarvam-translate:v1
        result_v2 = translate_text(
            text=text,
            source_language_code="en-IN",
            target_language_code="hi-IN",
            model="sarvam-translate:v1"
        )
        
        print(f"Original: {text}")
        print(f"mayura:v1: {result_v1.translated_text}")
        print(f"sarvam-translate:v1: {result_v2.translated_text}")
        
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 4: Using extended languages (only sarvam-translate:v1)
    print("\n" + "=" * 50)
    print("Example 4: Extended Languages (sarvam-translate:v1 only)")
    print("=" * 50)
    
    examples = [
        {
            "text": "धन्यवाद",  # Hindi
            "source": "hi-IN",
            "target": "ur-IN",
            "description": "Hindi to Urdu"
        },
        {
            "text": "स्वागतम्",  # Sanskrit
            "source": "sa-IN",
            "target": "en-IN",
            "description": "Sanskrit to English"
        },
        {
            "text": "আপোনাক স্বাগতম",  # Assamese
            "source": "as-IN",
            "target": "hi-IN",
            "description": "Assamese to Hindi"
        }
    ]
    
    for example in examples:
        try:
            result = translate_text(
                text=example["text"],
                source_language_code=example["source"],
                target_language_code=example["target"],
                model="sarvam-translate:v1"
            )
            print(f"\n{example['description']}:")
            print(f"  Original: {example['text']}")
            print(f"  Translated: {result.translated_text}")
        except Exception as e:
            print(f"\n{example['description']}: Error - {e}")
    
    # Example 5: Formal vs Informal translation
    print("\n" + "=" * 50)
    print("Example 5: Formal vs Informal Translation")
    print("=" * 50)
    
    text = "How are you doing today?"
    
    try:
        formal_result = translate_text(
            text=text,
            source_language_code="en-IN",
            target_language_code="hi-IN",
            mode="formal",
            model="sarvam-translate:v1"
        )
        
        informal_result = translate_text(
            text=text,
            source_language_code="en-IN",
            target_language_code="hi-IN",
            mode="informal",
            model="sarvam-translate:v1"
        )
        
        print(f"Original: {text}")
        print(f"Formal: {formal_result.translated_text}")
        print(f"Informal: {informal_result.translated_text}")
        
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 6: Gender-based translation
    print("\n" + "=" * 50)
    print("Example 6: Gender-based Translation")
    print("=" * 50)
    
    text = "I am happy"
    
    try:
        male_result = translate_text(
            text=text,
            source_language_code="en-IN",
            target_language_code="hi-IN",
            speaker_gender="Male",
            model="sarvam-translate:v1"
        )
        
        female_result = translate_text(
            text=text,
            source_language_code="en-IN",
            target_language_code="hi-IN",
            speaker_gender="Female",
            model="sarvam-translate:v1"
        )
        
        print(f"Original: {text}")
        print(f"Male: {male_result.translated_text}")
        print(f"Female: {female_result.translated_text}")
        
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
