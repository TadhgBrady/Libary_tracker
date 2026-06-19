from abc import ABC, abstractmethod
from typing import List
from app.domain.entities.book import Book

class BookRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Book]:
        pass

    @abstractmethod
    def create(self, book: Book) -> Book:
        pass