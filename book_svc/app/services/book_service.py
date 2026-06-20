from app.domain.entities.book import Book
from app.domain.repositories.book_repository import BookRepository
from app.decorators.logging import log_execution
from app.core.errors import NotFoundError


class BookService:
    def __init__(self, repo: BookRepository):
        self.repo = repo

    @log_execution
    def get_all_books(self) -> list[Book]:
        return self.repo.get_all()

    @log_execution
    def get_book(self, book_id: int) -> Book:
        book = self.repo.get_by_id(book_id)
        if book is None:
            raise NotFoundError(f"Book with id {book_id} not found")
        return book

    @log_execution
    def create_book(self, data: dict) -> Book:
        book = Book(**data)
        return self.repo.create(book)