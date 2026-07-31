from src.summarizer import summarize_text


text = """
The Eiffel Tower, located in Paris, France,
was constructed between 1887 and 1889 as the entrance arch
to the 1889 World's Fair.

It was designed by Gustave Eiffel's engineering company.
Today it attracts over 7 million visitors annually.
"""


summary = summarize_text(text)

print(summary)