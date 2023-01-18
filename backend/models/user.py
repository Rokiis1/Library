from typing import Optional
from pydantic import BaseModel as PydanticBaseModel, validator


class User(PydanticBaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    hashed_password: str
    repeat_password: str
    is_active: bool = True
    
    
    @validator("username", pre=True)
    def username_min_length(cls, value):
        if value and len(value) < 6:
            raise ValueError("Username must be at least 6 characters long.")
        return value

    @validator("hashed_password", pre=True)
    def password_min_length(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        return value
