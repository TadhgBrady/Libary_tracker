from pydantic import BaseModel
from datetime import datetime

class CommentCreate(BaseModel):
    content: str

class CommentResponse(BaseModel):
    id: int
    content: str
    book_id: int
    created_at: datetime

    class Config:
        from_attributes = True

class BookCreate(BaseModel):
    title: str
    author: str
    genre: str | None = None
    year_published: int | None = None
    isbn: str | None = None
    rating: float | None = None
    read: bool = False

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    genre: str | None = None
    year_published: int | None = None
    isbn: str | None = None
    rating: float | None = None
    read: bool
    comments: list[CommentResponse] = []

    class Config:
        from_attributes = True
