# tts/tts.py

from gtts import gTTS
from playsound import playsound
import uuid
import os


def text_to_speech(text: str):
    """
    Convert Bengali text to speech and play it.
    """

    if not text or not text.strip():
        return

    print(f"🔊 AI (বাংলা): {text}")

    filename = f"tts_{uuid.uuid4()}.mp3"

    try:
        tts = gTTS(text=text, lang="bn")
        tts.save(filename)
        playsound(filename)
    except Exception as e:
        print("❌ TTS সমস্যা:", e)
    finally:
        if os.path.exists(filename):
            os.remove(filename)
