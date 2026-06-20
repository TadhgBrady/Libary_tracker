from sqlalchemy.exc import SQLAlchemyError
from app.domain.entities.book import Book as DomainBook
from app.domain.repositories.book_repository import BookRepository
from app.infra.db.models import Book as DBBook
from app.core.errors import DatabaseError


class SQLBookRepository(BookRepository):

    def __init__(self, db):
        self.db = db

    def get_all(self):
        return self.db.query(DBBook).all()

    def get_by_id(self, book_id: int):
        return self.db.query(DBBook).filter(DBBook.id == book_id).first()

    def create(self, book: DomainBook):
        try:
            db_book = DBBook(**book.__dict__)
            self.db.add(db_book)
            self.db.commit()
            self.db.refresh(db_book)
            return db_book

        except SQLAlchemyError as e:
            self.db.rollback()
            raise DatabaseError(str(e))

    def update(self, book: DomainBook):
        try:
            self.db.commit()
            self.db.refresh(book)
            return book

        except SQLAlchemyError as e:
            self.db.rollback()
            raise DatabaseError(str(e))
        
    def delete(self, book_id: int):
        try:
            db_book = (
                self.db.query(DBBook)
                .filter(DBBook.id == book_id)
                .first()
            )

            if db_book:
                self.db.delete(db_book)
                self.db.commit()

        except SQLAlchemyError as e:
            self.db.rollback()
            raise DatabaseError(str(e))