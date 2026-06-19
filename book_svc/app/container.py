from fastapi import Depends
from sqlalchemy.orm import Session

from app.interfaces.api.deps import get_db
from app.infra.repositories.book_repo_sql import SQLBookRepository
from app.services.book_service import BookService

def get_book_service(db: Session= Depends(get_db)):
    repo = SQLBookRepository(db)
    return BookService(repo)