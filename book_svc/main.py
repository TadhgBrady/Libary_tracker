from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from model import *
app = FastAPI()

books = []
"Returns a list of all books in the library"
@app.get("/books")
async def get_books():
    return {"books": books}

"Creates a new book in the library"
@app.post("/books")
async def create_book(book: Book):
    books.append(book)
    return {"message": "book added", "book": book}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1",port=8001)