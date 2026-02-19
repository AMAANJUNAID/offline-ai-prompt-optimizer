import re


def normalize_output(text):
    """
    Remove markdown formatting that breaks parsing.
    """
    text = text.replace("##", "")
    text = text.replace("**", "")
    return text


def extract_between(text, start_keyword, end_keywords):
    start_match = re.search(start_keyword, text, re.IGNORECASE)
    if not start_match:
        return ""

    start_index = start_match.end()
    end_index = len(text)

    for keyword in end_keywords:
        match = re.search(keyword, text[start_index:], re.IGNORECASE)
        if match:
            candidate_end = start_index + match.start()
            if candidate_end < end_index:
                end_index = candidate_end

    return text[start_index:end_index].strip()


def extract_score(keyword, text, max_value):
    pattern = rf"{keyword}[^0-9]*(\d+)"
    match = re.search(pattern, text, re.IGNORECASE)
    if not match:
        return "0"

    value = int(match.group(1))
    return str(min(value, max_value))


def parse_model_output(output: str) -> dict:
    result = {}

    # Normalize markdown
    output = normalize_output(output)

    # Extract refined prompt
    refined = extract_between(
        output,
        r"REFINED PROMPT:",
        ["INTENT SUMMARY", "EXPECTED OUTPUT FORMAT", "EDGE CASES", "SCORES", "USER INPUT"]
    )

    result["refined"] = refined if refined else output.strip()

    # Extract scores
    result["clarity"] = extract_score("clar", output, 10)
    result["structure"] = extract_score("struct", output, 10)
    result["completeness"] = extract_score("complete", output, 10)
    result["confidence"] = extract_score("confid", output, 100)

    return result
