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
    target_language_code: str = "hi-IN"
):
    """
    Translate text between languages.
    
    Args:
        text: The text to translate
        source_language_code: Source language code (default: auto)
        target_language_code: Target language code
    
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
        target_language_code=target_language_code
    )
    
    return response


def main():
    """Example usage of text translation API."""
    
    # Example 1: Basic translation with auto-detect
    print("=" * 50)
    print("Example 1: Auto-detect and Translate")
    print("=" * 50)
    
    text = "Hello, how are you?"
    
    try:
        result = translate_text(
            text=text,
            source_language_code="auto",
            target_language_code="hi-IN"
        )
        print(f"Original: {text}")
        print(f"Translated (Hindi): {result.translated_text}")
        
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 2: Using all 22 languages
    print("\n" + "=" * 50)
    print("Example 2: Translate to All 22 Languages")
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
        # Additional 11 languages
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
                target_language_code=lang_code
            )
            print(f"{lang_name:12} ({lang_code:8}): {result.translated_text}")
        except Exception as e:
            print(f"{lang_name:12} ({lang_code:8}): Error - {e}")
    
    # Example 3: Extended languages translations
    print("\n" + "=" * 50)
    print("Example 3: Extended Languages")
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
                target_language_code=example["target"]
            )
            print(f"\n{example['description']}:")
            print(f"  Original: {example['text']}")
            print(f"  Translated: {result.translated_text}")
        except Exception as e:
            print(f"\n{example['description']}: Error - {e}")


if __name__ == "__main__":
    main()
