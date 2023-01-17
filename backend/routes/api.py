from fastapi import FastAPI, HTTPException
from models.user import User
from services import user_service

router = FastAPI().router


@router.post("/register")
async def register(user: User):
    """
    register user
    """
    try:
        result = await user_service.register(user)
        return result
    except HTTPException as e:
        raise e
