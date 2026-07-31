from src.splitter import split_text

text = """
The Eiffel Tower, located in Paris, France, was constructed between 1887 and 1889.
It was designed by Gustave Eiffel's engineering company.
"""

chunks = split_text(text, 50)

for chunk in chunks:
    print("-----")
    print(chunk)