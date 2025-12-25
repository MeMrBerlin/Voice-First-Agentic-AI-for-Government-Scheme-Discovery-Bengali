# main.py

from stt.stt import speech_to_text
from tts.tts import text_to_speech

from agent.planner import plan
from agent.executor import execute
from agent.evaluator import evaluate

from memory.session_store import SessionMemory
from utils.input_validation import extract_digits, is_valid_text, interpret_income


# -------------------------
# Question prompts (Bengali)
# -------------------------
QUESTIONS = {
    "ASK_AGE": "আপনার বয়স কত? (শুধু সংখ্যা বলুন, যেমন: ৩০)",
    "ASK_INCOME": "আপনার বার্ষিক আয় কত? (শুধু সংখ্যা বলুন, যেমন: ৫)",
    "ASK_OCCUPATION": "আপনার পেশা কী? (farmer / other)",
    "ASK_STATE": "আপনি কোন রাজ্যে থাকেন?"
}

FIELD_MAP = {
    "ASK_AGE": "age",
    "ASK_INCOME": "income",
    "ASK_OCCUPATION": "occupation",
    "ASK_STATE": "state"
}


def run_agent():
    """
    Main agent loop.
    """

    memory = SessionMemory()

    # Greeting
    text_to_speech("আমি একটি সরকারি প্রকল্প সহায়ক। আমি আপনাকে সাহায্য করব।")

    while True:
        # -------- Planner --------
        action = plan(memory)

        # -------- Ask user --------
        if action.startswith("ASK"):
            field = FIELD_MAP[action]
            question = QUESTIONS[action]

            text_to_speech(question)

            user_input = speech_to_text()

            # Silence or invalid speech
            if not is_valid_text(user_input):
                text_to_speech("আমি শুনতে পাইনি। অনুগ্রহ করে আবার বলুন।")
                continue

            # -------- Age handling --------
            if field == "age":
                number = extract_digits(user_input)
                if not number:
                    text_to_speech("বয়স স্পষ্ট নয়। অনুগ্রহ করে শুধু সংখ্যা বলুন।")
                    continue
                user_input = number

            # -------- Income handling (Lakhs logic) --------
            if field == "income":
                income_value = interpret_income(user_input)
                if not income_value:
                    text_to_speech("আয়ের পরিমাণ স্পষ্ট নয়। অনুগ্রহ করে আবার বলুন।")
                    continue
                user_input = income_value

            # -------- Contradiction handling --------
            contradiction, old_value = memory.detect_contradiction(field, user_input)
            if contradiction:
                text_to_speech(
                    f"আপনি আগে বলেছিলেন {old_value}, এখন বলছেন {user_input}। অনুগ্রহ করে নিশ্চিত করুন।"
                )
                continue

            memory.update(field, user_input)
            continue

        # -------- Execute tools --------
        if action == "CHECK_ELIGIBILITY":
            execution_result = execute(action, memory)

            # -------- Evaluate --------
            evaluation = evaluate(execution_result)

            if evaluation == "NO_ELIGIBLE_SCHEME":
                text_to_speech("দুঃখিত, আপনার জন্য কোনো উপযুক্ত সরকারি প্রকল্প পাওয়া যায়নি।")
                break

            if evaluation == "ERROR":
                text_to_speech("একটি সমস্যা হয়েছে। অনুগ্রহ করে পরে আবার চেষ্টা করুন।")
                break

            if evaluation == "SUCCESS":
                scheme = execution_result["scheme"]

                text_to_speech(f"আপনি এই প্রকল্পের জন্য যোগ্য: {scheme['name']}")
                text_to_speech(scheme["description"])
                text_to_speech(f"সুবিধা: {scheme['benefits']}")
                text_to_speech(
                    "প্রয়োজনীয় নথি হলো: " + ", ".join(scheme["documents"])
                )
                break


# -------------------------
# Entry point
# -------------------------
if __name__ == "__main__":
    run_agent()
