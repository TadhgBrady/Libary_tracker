class FakeDB:
    def __init__(self):
        self.books = []
    
    def add(self, book):
        self.books.append(book)
        
    def commit(self):
        pass

    def refresh(self, book):
        pass
    
    def query(self, model):
        return fakeQuery(self.books)
    
class fakeQuery:
    def __init__(self, books):
        self.books = books
    
    def all(self):
        return self.books
    
    def filter_by(self, **kwargs):
        filtered_books = [book for book in self.books if all(getattr(book, k) == v for k, v in kwargs.items())]
        return fakeQuery(filtered_books)
    
    def first(self):
        return self.books[0] if self.books else None


def override_get_db():
    db = FakeDB()
    try:
        yield db
    finally:
        pass