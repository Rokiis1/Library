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
    is_active: bool = True

    @validator("hashed_password", "repeat_password", pre=True)
    def validate_passwords(cls, value, values):
        if "hashed_password" in values and "repeat_password" in values:
            hashed_password = values["hashed_password"]
            repeat_password = values["repeat_password"]
            if hashed_password != repeat_password:
                raise ValueError("Passwords do not match")
        if len(hashed_password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not any(c.isupper() for c in hashed_password):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(c.islower() for c in hashed_password):
            raise ValueError("Password must contain at least one lowercase letter")
        if not any(c.isdigit() for c in hashed_password):
            raise ValueError("Password must contain at least one number")
        if not any(c in "!@#$%^&*()_+-=[]{};:'\"\\|,.<>/?`~" for c in hashed_password):
            raise ValueError("Password must contain at least one symbol")
        return value
