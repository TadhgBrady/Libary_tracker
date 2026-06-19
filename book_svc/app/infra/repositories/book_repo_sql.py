from sqlalchemy.exc import SQLAlchemyError
from app.domain.entities.book import Book
from app.domain.repositories.book_repository import BookRepository
from app.infra.db.models import Book
from app.core.errors import DatabaseError

class SQLBookRepository(BookRepository):

    def __init__(self, db):
        self.db = db

    def get_all(self):
        return self.db.query(Book).all()

    def get_by_id(self,book):
        return self.db.query(Book)

    def create(self, book: Book):
        try:
            db_book = Book(**book.__dict__)
            self.db.add(db_book)
            self.db.commit()
            self.db.refresh(db_book)
            return db_book  
    
        except SQLAlchemyError as e:
            self.db.rollback()
            raise DatabaseError(str(e))
