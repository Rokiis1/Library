from typing import Optional
from pydantic import BaseModel, validator


class Book(BaseModel):
    title: str
    author: str
    year: int
    image: Optional[str] = None
