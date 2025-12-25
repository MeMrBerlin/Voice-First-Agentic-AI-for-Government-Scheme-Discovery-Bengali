# Voice-First Agentic AI for Government Scheme Discovery (Bengali)

## Overview
This project is a **terminal-based, voice-first, agentic AI system** that helps users
identify eligible **Indian government welfare schemes** using **Bengali voice interaction**.

The system is **not a chatbot**. It demonstrates a **true agentic workflow**
with planning, tool usage, memory, and failure handling, as required by the assignment.

---

## Key Features

- 🎤 **Voice-first interaction**
  - User speaks via microphone
  - Agent responds via spoken Bengali

- 🌐 **Native Language Support**
  - End-to-end Bengali pipeline (STT → Agent → TTS)

- 🧠 **Agentic AI Architecture**
  - Planner → Executor → Evaluator loop
  - Dynamic decision-making
  - Multi-turn reasoning

- 🛠️ **Tool Usage**
  - Eligibility Engine (tool)
  - Scheme Database (tool)

- 🧾 **Conversation Memory**
  - Stores user details across turns
  - Detects contradictory answers

- ⚠️ **Failure Handling**
  - Handles silence
  - Handles unclear speech
  - Handles invalid numeric input
  - Graceful recovery without crashing

---

## Architecture
- **main.py**: Main entry point, orchestrates the agent loop.
- **agent/planner.py**: Decides the next action based on memory state.
- **agent/executor.py**: Executes actions by invoking tools.
- **agent/evaluator.py**: Evaluates execution results and determines outcomes.
- **memory/session_store.py**: Handles session data storage and validation.
- **stt/stt.py**: Handles speech-to-text conversion.
- **tts/tts.py**: Manages text-to-speech output.
- **tools/eligibility.py**: Checks user eligibility for schemes.
- **tools/scheme_db.py**: Provides scheme details.
- **utils/input_validation.py**: Validates and processes user input.


---

## Setup Instructions

### Prerequisites
- Python 3.9 or higher
- Microphone access for voice input

### 1. Create and activate virtual environment

```powershell
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### How to Run
- From the project root directory:

```
python main.py

```


## How the Agent Works

1. The agent greets the user in **Bengali using voice output**.
2. The agent asks questions **one by one** using voice:
   - Age  
   - Income  
   - Occupation  
   - State  
3. The user responds to each question using **voice input**.
4. The agent stores all responses in **conversation memory**.
5. Once all required information is collected, the agent invokes the **eligibility engine tool**.
6. The agent retrieves relevant scheme details from the **scheme database tool**.
7. The agent speaks the **eligible government scheme information in Bengali**.

---

## Example Interaction

- **Agent:** “আপনার বয়স কত?”  
- **User:** “৬৫”  

- **Agent:** “আপনার বার্ষিক আয় কত?”  
- **User:** “১২০০০০”  

- **Agent:** “আপনি এই প্রকল্পের জন্য যোগ্য: বার্ধক্য ভাতা প্রকল্প”


## Dependencies
- openai-whisper: For speech recognition.
- torch: Machine learning framework.
- sounddevice, scipy, numpy: Audio processing.
- gTTS, playsound: Text-to-speech.
- uuid: For temporary file generation.

