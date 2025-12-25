# tools/scheme_db.py

"""
Scheme Database Tool
--------------------
This module stores information about government welfare schemes.
The agent retrieves scheme details using this tool.
All content is in Bengali.
"""

SCHEMES = {
    "OLD_AGE_PENSION": {
        "name": "বার্ধক্য ভাতা প্রকল্প",
        "description": "৬০ বছর বা তার বেশি বয়সী নাগরিকদের জন্য আর্থিক সহায়তা।",
        "benefits": "মাসে ₹১০০০ আর্থিক সহায়তা",
        "documents": [
            "আধার কার্ড",
            "বয়সের প্রমাণপত্র",
            "ব্যাংক অ্যাকাউন্ট বিবরণ"
        ]
    },
    "PM_KISAN": {
        "name": "প্রধানমন্ত্রী কিসান সম্মান নিধি",
        "description": "ছোট ও প্রান্তিক কৃষকদের জন্য আয় সহায়তা প্রকল্প।",
        "benefits": "বছরে ₹৬০০০ (৩ কিস্তিতে)",
        "documents": [
            "আধার কার্ড",
            "ব্যাংক অ্যাকাউন্ট বিবরণ",
            "জমির কাগজ"
        ]
    }
}


def get_scheme_details(scheme_key: str):
    """
    Retrieve scheme details by key.
    Returns None if scheme not found.
    """
    return SCHEMES.get(scheme_key)
