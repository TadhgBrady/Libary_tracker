from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    genre: str | None = None
    year_published: int | None = None
    isbn: str | None = None
    rating: float | None = None
    read: bool = False

@dataclass
class Comment:
    content: str
    book_id: int
    id: int | None = None