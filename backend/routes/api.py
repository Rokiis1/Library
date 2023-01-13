from fastapi import FastAPI
from models.user import User
from services import user_service

router = FastAPI().router


@router.post("/register")
async def register(user: User):
    """
    register user
    """
    return await user_service.register(user)


@router.post("/login")
async def login(user: User):
    """
    login user
    """
    return await user_service.login(user)
