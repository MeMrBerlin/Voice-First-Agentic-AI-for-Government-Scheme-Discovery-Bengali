# utils/input_validation.py

"""
Input Validation Utilities
--------------------------
Helps clean and validate user inputs coming from speech.
"""


def extract_digits(text: str):
    """
    Extract digits from a string.
    Returns a digit string or None if no digits found.
    """
    if not text:
        return None

    digits = "".join(ch for ch in text if ch.isdigit())
    return digits if digits else None


def is_valid_text(text: str):
    """
    Check if text is non-empty and meaningful.
    """
    if not text:
        return False

    if not text.strip():
        return False

    return True
