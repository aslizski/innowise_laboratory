from pydantic import BaseModel
from typing import Optional


class BookIn(BaseModel):
    title: str
    author: str
    year: Optional[int] = None


class BookOut(BookIn):
    id: int

    class Config:
        orm_mode = True
