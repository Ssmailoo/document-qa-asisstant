def chunk_text(text: str, chunk_size: int, overlap: int) -> list[str]:
    words = text.split()

    if not words:
        raise ValueError("Document contains no text.")
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0.")
    if overlap < 0 or overlap >= chunk_size:
        raise ValueError ("overlap must be between 0 and chunk_size - 1.")

    step = chunk_size - overlap

    start = 0
    chunks = []

    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += step

    return chunks
