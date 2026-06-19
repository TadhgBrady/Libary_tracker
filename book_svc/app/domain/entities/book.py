from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    genre: str | None = None
    year_published: int | None = None