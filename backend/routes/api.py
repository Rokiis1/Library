from fastapi import FastAPI, HTTPException
from services import book_service
from models.book import Book
from models.user import RegisterUser, LoginUser
from services import user_service


router = FastAPI().router


@router.post("/register")
async def register(user: RegisterUser):
    """
    register user
    """
    try:
        result = await user_service.register(user)
        return result
    except HTTPException as e:
        raise e


@router.post("/login")
async def login(user: LoginUser):
    """
    login user
    """
    try:
        result = await user_service.login(user)
        return result
    except HTTPException as e:
        raise e


@router.get("/books/")
async def read_all_books():
    try:
        result = await book_service.read_all_books()
        return result
    except HTTPException as e:
        raise e


@router.get("/books/{book_id}")
async def read_book(book_id: int):
    try:
        result = await book_service.read_book(book_id)
        return result
    except HTTPException as e:
        raise e


@router.post("/book")
async def create_book(book: Book):
    try:
        result = await book_service.create_book(book)
        return result
    except HTTPException as e:
        raise e


@router.put("/books/{book_id}")
async def update_whole_book(book_id: int, book: Book):
    try:
        result = await book_service.update_all_book(book_id, book)
        return result
    except HTTPException as e:
        raise e


@router.delete("/books/{book_id}")
async def delete_book(book_id: int):
    try:
        result = await book_service.delete_book(book_id)
        return result
    except HTTPException as e:
        raise e


@router.patch("/books/{book_id}")
async def update_book(book_id: int, updates: dict):
    try:
        result = await book_service.update_book(book_id, updates)
        return result
    except HTTPException as e:
        raise e
