"""
This is translator between English and French
"""
from deep_translator import MyMemoryTranslator as Mem

def english_to_french(english_text):
    """
    This function translate English to French
    """
    french_text = Mem(source='en-GB', target='fr-FR').translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    This function translate French to English
    """
    english_text = Mem(source='fr-FR', target='en-GB').translate(french_text)
    return english_text
