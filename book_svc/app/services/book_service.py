from app.domain.entities.book import Book
from app.infra.repositories.book_repo_sql import SQLBookRepository
from app.decorators.logging import log_execution

class BookService:
    def __init__(self, repo: SQLBookRepository):
        self.repo = repo
    
    @log_execution 
    def get_all_books(self):
        return self.repo.get_all()
    
    @log_execution
    def create_book(self,data: dict):
        book = Book(**data)
        return self.repo.create(book)