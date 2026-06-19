from app.domain.entities.book import Book

class CreateBook:
    def __init__(self,repo):
        self.repo = repo
    
    def execute(self,payload):
        book = Book(**payload.model_dump())
        return self.repo.create(book)