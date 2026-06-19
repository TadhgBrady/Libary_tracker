from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    genre: str | None = None
    year_published: int | None = None

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    genre: str | None = None
    year_published: int | None = None

class Config:
    from_attributes = True
