# autocorrect_logic.py
from autocorrect import Speller

spell = Speller(lang='en')

def autocorrect_text(input_text: str) -> str:
    """Return the autocorrected version of the input text using autocorrect.Speller."""
    if not input_text.strip():
        return ""
    # Correct each word individually
    words = input_text.split()
    corrected_words = [spell(word) for word in words]
    return " ".join(corrected_words)