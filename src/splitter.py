def split_text(text, chunk_size=1000):
    """
    Fixed-size splitting strategy.
    Splits text into chunks of a fixed number of characters.
    """

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks