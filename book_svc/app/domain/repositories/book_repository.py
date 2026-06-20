from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.book import Book


class BookRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Book]:
        pass

    @abstractmethod
    def get_by_id(self, book_id: int) -> Optional[Book]:
        pass

    @abstractmethod
    def create(self, book: Book) -> Book:
        pass