from typing import Optional
from pydantic import BaseModel, validator


class LoginUser(BaseModel):
    email: Optional[str] = None
    hashed_password: str


class RegisterUser(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    hashed_password: str
    repeat_password: str

    @validator("hashed_password", "repeat_password", pre=True)
    def validate_passwords(cls, value, values):
        hashed_password = values.get("hashed_password")
        repeat_password = values.get("repeat_password")
        if "hashed_password" not in values or "repeat_password" not in values:
            return value
        if hashed_password != repeat_password:
            raise ValueError("Passwords do not match")
        if len(hashed_password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not any(c.isupper() for c in hashed_password) or not any(c.islower() for c in hashed_password) or not any(c.isdigit() for c in hashed_password) or not any(c in "!@#$%^&*()_+-=[]{};:'\"\\|,.<>/?`~" for c in hashed_password):
            raise ValueError("Password must contain at least one uppercase letter, one lowercase letter, one digit, and one symbol")
        return value
