from fastapi import APIRouter,Depends
from app.interfaces.api.deps import get_db
from app.interfaces.api.schemas.book import BookCreate, BookResponse
from app.infra.repositories.book_repo_sql import SQLBookRepository
from app.use_cases.get_books import GetBooks
from app.use_cases.create_book import CreateBook

router = APIRouter()

@router.get("/",response_model=list[BookResponse])
def get_books(db=Depends(get_db)):
    repo = SQLBookRepository(db)
    use_case = GetBooks(repo)
    return use_case.execute()
    
@router.post("/",response_model=BookResponse)
def create_book(payload:BookCreate, db=Depends(get_db)):
    repo = SQLBookRepository(db)
    use_case = CreateBook(repo)
    return use_case.execute(payload)