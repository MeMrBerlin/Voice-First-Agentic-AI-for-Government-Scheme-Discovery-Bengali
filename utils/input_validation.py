# utils/input_validation.py

"""
Input Validation Utilities
--------------------------
Handles numeric extraction and Indian income interpretation.
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


def interpret_income(text: str):
    """
    Interpret income from speech.
    
    Rules:
    - If user says a small number (<= 100), treat it as lakhs
      e.g., "15" -> 1500000
    - If user explicitly says lakh/lakhs, treat as lakhs
    - Otherwise, treat as raw number
    """

    if not text:
        return None

    text_lower = text.lower()

    digits = extract_digits(text)
    if not digits:
        return None

    value = int(digits)

    # Explicit lakh mention
    if "lakh" in text_lower or "lac" in text_lower:
        return str(value * 100000)

    # Heuristic: small numbers are likely lakhs
    if value <= 100:
        return str(value * 100000)

    # Otherwise, assume full amount spoken
    return str(value)


def is_valid_text(text: str):
    """
    Check if text is non-empty and meaningful.
    """
    if not text:
        return False

    if not text.strip():
        return False

    return True
