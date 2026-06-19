from app.domain.entities.book import Book
from app.domain.repositories.book_repository import BookRepository
from app.infra.db.models import Book
class SQLBookRepository(BookRepository):

    def __init__(self, db):
        self.db = db

    def get_all(self):
        return self.db.query(Book).all()

    def create(self, book: Book):
        db_book = Book(**book.__dict__)
        self.db.add(db_book)
        self.db.commit()
        self.db.refresh(db_book)
        return db_book