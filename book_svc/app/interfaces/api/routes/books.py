from fastapi import APIRouter,Depends
from app.interfaces.api.schemas.book import BookCreate, BookResponse, CommentCreate, CommentResponse
from app.container import get_book_service
from app.infra.db.session import get_db
from app.infra.db.models import Comment

router = APIRouter()

@router.get("/",response_model=list[BookResponse])
def get_books(service=Depends(get_book_service)):
    return service.get_all_books()
    
@router.post("/",response_model=BookResponse)
def create_book(
    payload:BookCreate,
    service=Depends(get_book_service)):
    return service.create_book(payload.model_dump())

@router.post("/{book_id}/comments",response_model=CommentResponse)
def add_comment(
    book_id:int,
    payload:CommentCreate,
    db=Depends(get_db)):
    comment = Comment(content=payload.content,book_id=book_id)
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

@router.get("/{book_id}/comments",response_model=list[CommentResponse])
def get_book_comments(
    book_id:int,
    db=Depends(get_db)):
    return db.query(Comment).filter_by(book_id=book_id).all()

@router.put("/{book_id}",response_model=BookResponse)
def update_book(
    book_id:int,
    payload:BookCreate,
    service=Depends(get_book_service)):
    return service.update_book(book_id, payload.model_dump())

@router.delete("/{book_id}")
def delete_book(
    book_id:int,
    service=Depends(get_book_service)):
    service.delete_book(book_id)
    return {"message": f"Book with id {book_id} deleted successfully"}