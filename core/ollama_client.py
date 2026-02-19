import subprocess
import os

MODEL_NAME = os.getenv("MODEL_NAME", "gemma:2b")

def run_ollama(prompt: str) -> str:
    import subprocess

    process = subprocess.run(
        ["ollama", "run", MODEL_NAME],
        input=prompt.encode("utf-8"),
        capture_output=True,
        timeout=180
    )

    output = process.stdout.decode("utf-8", errors="ignore")

    print("\n----- RAW MODEL OUTPUT -----\n")
    print(output)
    print("\n----------------------------\n")

    return output.strip()
