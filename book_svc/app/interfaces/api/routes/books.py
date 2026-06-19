from fastapi import APIRouter,Depends
from app.interfaces.api.schemas.book import BookCreate, BookResponse
from app.container import get_book_service

router = APIRouter()

@router.get("/",response_model=list[BookResponse])
def get_books(service=Depends(get_book_service)):
    return service.get_all_books()
    
@router.post("/",response_model=BookResponse)
def create_book(
    payload:BookCreate,
    service=Depends(get_book_service)):
    return service.create_book(payload.model_dump())