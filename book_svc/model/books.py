from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str
    isbn: str
    rating: float
    status: str

    def __str__(self):
        return (
            f"title: {self.title}\n"
            f"author: {self.author}\n"
            f"isbn: {self.isbn}\n"
            f"status: {self.status}\n"
            f"rating: {self.rating}"
        )

    def __repr__(self):
        return self.__str__()