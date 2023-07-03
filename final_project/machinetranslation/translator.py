"""
This is translator between English and French
"""
from deep_translator import MyMemoryTranslator as Mem

def english_to_french(english_text):
    """
    This function translate English to French
    """
    french_text = Mem(source='en', target='fr').translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    This function translate French to English
    """
    english_text = Mem(source='fr', target='en').translate(french_text)
    return english_text
