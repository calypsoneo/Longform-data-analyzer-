from src.extractor import extract_facts


text = """
The Eiffel Tower, located in Paris, France,
was constructed between 1887 and 1889.
It was designed by Gustave Eiffel's engineering company.
"""

result = extract_facts(text)

print(result)


