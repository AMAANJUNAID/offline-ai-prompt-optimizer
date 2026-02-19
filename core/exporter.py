import os
from datetime import datetime

EXPORT_DIR = "exports"


def export_result(content: str) -> str:
    if not os.path.exists(EXPORT_DIR):
        os.makedirs(EXPORT_DIR)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"refined_prompt_{timestamp}.txt"
    filepath = os.path.join(EXPORT_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return filepath
