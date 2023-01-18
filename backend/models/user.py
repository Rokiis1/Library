from typing import Optional
from pydantic import BaseModel as PydanticBaseModel


class User(PydanticBaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    hashed_password: str
    repeat_password: str
    is_active: bool = True
