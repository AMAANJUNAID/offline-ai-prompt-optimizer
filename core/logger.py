from datetime import datetime

HISTORY_FILE = "history.txt"


def log_interaction(user_prompt: str, model_output: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write(f"Timestamp: {timestamp}\n\n")
        f.write("USER PROMPT:\n")
        f.write(user_prompt + "\n\n")
        f.write("MODEL OUTPUT:\n")
        f.write(model_output + "\n\n")
