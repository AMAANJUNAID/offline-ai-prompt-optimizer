from flask import Flask, render_template, request, send_from_directory, url_for
import os

from core.optimizer import build_structured_prompt
from core.ollama_client import run_ollama
from core.exporter import export_result
from core.logger import log_interaction
from core.parser import parse_model_output

app = Flask(__name__)

EXPORT_FOLDER = "exports"

@app.route("/history")
def history():
    history_content = ""

    if os.path.exists("history.txt"):
        with open("history.txt", "r", encoding="utf-8") as f:
            history_content = f.read()

    return render_template("history.html", history=history_content)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/optimizer", methods=["GET", "POST"])
def optimizer():
    result = None
    error = None
    export_filename = None

    if request.method == "POST":
        raw_prompt = request.form.get("prompt")

        if not raw_prompt or raw_prompt.strip() == "":
            error = "Prompt cannot be empty."
        else:
            try:
                structured_prompt = build_structured_prompt(raw_prompt)
                model_output = run_ollama(structured_prompt)

                log_interaction(raw_prompt, model_output)

                export_path = export_result(model_output)
                export_filename = os.path.basename(export_path)

                result = parse_model_output(model_output)

            except Exception as e:
                error = str(e)

    return render_template(
        "optimizer.html",
        result=result,
        error=error,
        export_filename=export_filename
    )


@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(EXPORT_FOLDER, filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
