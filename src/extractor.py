import requests
import json


def extract_facts(chunk):
    """
    Sends document chunks to Ollama
    and extracts important facts.
    """

    prompt = f"""
You are a knowledge extraction assistant.

Extract the following from the text:

- People
- Places
- Dates
- Numbers
- Events

Return the answer in JSON format.

Text:
{chunk}
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