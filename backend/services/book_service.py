from fastapi import HTTPException
from database import database_manager
from models.book import Book


async def read_book(book_id: int):
    conn = await database_manager.get_connection()
    try:
        query = "SELECT * FROM books WHERE id = $1"
        result = await conn.fetchrow(query, book_id)
        if not result:
            raise HTTPException(status_code=404, detail="Book not found")
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="An error occurred while reading the book"
        ) from e
    finally:
        await conn.close()


async def read_all_books():
    conn = await database_manager.get_connection()
    try:
        query = "SELECT * FROM books"
        result = await conn.fetch(query)
        return [Book(**book) for book in result]
    except Exception as e:
        raise e
    finally:
        await conn.close()


async def create_book(book: Book):
    conn = await database_manager.get_connection()
    try:
        query = "INSERT INTO books (title, author, year, image) VALUES ($1, $2, $3, $4) RETURNING id"
        result = await conn.fetchrow(
            query, book.title, book.author, book.year, book.image
        )
        book_id = result["id"]
        return {"message": "Book created successfully", "book_id": book_id}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="An error occurred while creating the book"
        ) from e
    finally:
        await conn.close()


async def update_all_book(book_id: int, book: Book):
    conn = await database_manager.get_connection()
    try:
        query = "UPDATE books SET title = $1, author = $2, year = $3, image = $4 WHERE id = $5"
        await conn.execute(
            query, book.title, book.author, book.year, book.image, book_id
        )
        return {"message": "Book updated successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="An error occurred while updating the book"
        ) from e
    finally:
        await conn.close()


async def delete_book(book_id: int):
    conn = await database_manager.get_connection()
    try:
        query = "DELETE FROM books WHERE id=$1"
        await conn.execute(query, book_id)
        return {"message": "Book deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="An error occurred while deleting the book"
        ) from e
    finally:
        await conn.close()


async def update_book(book_id: int, updates: dict):
    conn = await database_manager.get_connection()
    try:
        query = "UPDATE books SET "
        for key, value in updates.items():
            query += f"{key} = '{value}', "
        query = query[:-2] + f" WHERE id = {book_id}"
        await conn.execute(query)
        return {"message": "Book updated successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="An error occurred while updating the book"
        ) from e
    finally:
        await conn.close()
