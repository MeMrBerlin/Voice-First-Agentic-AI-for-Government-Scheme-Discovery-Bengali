# stt/stt.py

import whisper
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import uuid
import os

# Load Whisper model once
model = whisper.load_model("small")

# CHANGE THIS if needed (we will verify mic later)
MIC_DEVICE_INDEX = None  # Set to an integer if default mic fails

SAMPLE_RATE = 16000


def speech_to_text():
    """
    Push-to-talk Speech-to-Text.
    User presses ENTER to start speaking
    and CTRL+C to stop.
    Returns transcribed Bengali text or empty string.
    """

    input("🎤 ENTER চাপুন, তারপর কথা বলুন... ")

    print("🎙️ কথা বলুন (শেষ হলে Ctrl+C চাপুন)")

    audio_chunks = []

    try:
        with sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype=np.float32,
            device=MIC_DEVICE_INDEX,
        ) as stream:
            while True:
                data, _ = stream.read(1024)
                audio_chunks.append(data)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print("❌ মাইক্রোফোন সমস্যা:", e)
        return ""

    if not audio_chunks:
        return ""

    audio = np.concatenate(audio_chunks, axis=0)

    filename = f"temp_{uuid.uuid4()}.wav"
    write(filename, SAMPLE_RATE, audio)

    try:
        result = model.transcribe(filename, language="bn")
        text = result.get("text", "").strip()
    except Exception as e:
        print("❌ ট্রান্সক্রিপশন সমস্যা:", e)
        text = ""
    finally:
        if os.path.exists(filename):
            os.remove(filename)

    if text == "":
        print("⚠️ কিছু শোনা যায়নি")
        return ""

    print("📝 শোনা হয়েছে:", text)
    return text
