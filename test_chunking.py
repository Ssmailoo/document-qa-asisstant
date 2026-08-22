import pytest
from chunking import chunk_text

def test_chunk():
    result = chunk_text(
        text="I go to work, I work at Huabao as a mechanic welder",
        chunk_size=5,
        overlap=2,
    )

    assert result == [
        "I go to work, I",
        "work, I work at Huabao",
        "at Huabao as a mechanic",
        "a mechanic welder",
    ]

def test_chunk_rejects_invalid_chunk_size():
    with pytest.raises(ValueError):
        chunk_text(
            text="I go to work, I work at Huabao as a mechanic welder",
            chunk_size=0,
            overlap=0,
        )

def test_chunk_rejects_invalid_overlap():
    with pytest.raises(ValueError):
        chunk_text(
            text="I go to work, I work at Huabao as a mechanic welder",
            chunk_size=5,
            overlap=5,
        )

def test_chunk_rejects_negative_overlap():
    with pytest.raises(ValueError):
        chunk_text(
            text="I go to work, I work at Huabao as a mechanic welder",
            chunk_size=5,
            overlap=-1,
        )

def test_chunk_rejects_empty_text():
    with pytest.raises(ValueError):
        chunk_text(
            text="",
            chunk_size=5,
            overlap=2,
        )

def test_chunk_handles_short_document():
    result = chunk_text(
        text="I go to",
        chunk_size=5,
        overlap=2,
    )
    assert result == [
        "I go to",
    ]
