from fastapi import HTTPException
import pytest
from services.book_service import read_book

@pytest.mark.asyncio
async def test_read_book():
    # Test successful read
    book = await read_book(4)
    assert dict(book) == {"id": 4, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951, "image": "https://images.penguinrandomhouse.com/cover/9780316769488"}

@pytest.mark.asyncio
async def test_read_book_not_found():
    # Test read book An error occurred while reading the book
    with pytest.raises(HTTPException) as e:
        await read_book(100)
    assert e.value.status_code == 500
    assert e.value.detail == "An error occurred while reading the book"