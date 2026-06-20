from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.infra.db.base import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    genre = Column(String)
    year_published = Column(Integer)
    isbn = Column(String, unique=True, index=True)
    rating = Column(Float)
    read = Column(Boolean, default=False)
    comments = relationship("Comment", back_populates="book", cascade="all, delete-orphan")

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    book_id = Column(Integer, ForeignKey("books.id"), index=True)
    created_at = Column(DateTime, server_default=func.now())
    book = relationship("Book", back_populates="comments")