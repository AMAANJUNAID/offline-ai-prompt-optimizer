def build_structured_prompt(user_prompt: str) -> str:
    return f"""
You are an AI prompt optimization assistant.

You MUST generate content for ALL sections below.
Do not leave any section empty.

Return in this exact format:

REFINED PROMPT:
<fully rewritten professional version>

INTENT SUMMARY:
<clear explanation>

EXPECTED OUTPUT FORMAT:
<describe structure of final answer>

EDGE CASES:
- <edge case 1>
- <edge case 2>

SCORES:
Clarity: X/10
Structure: X/10
Completeness: X/10
Confidence: X%

USER INPUT:
{user_prompt}
"""
