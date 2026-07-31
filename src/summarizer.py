import requests


def summarize_text(text):
    """
    Generates a short summary using Ollama.
    """

    prompt = f"""
Summarize the following document in a short paragraph.
Keep only the important information.

Document:
{text}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi3:mini",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()

    return result["response"]
