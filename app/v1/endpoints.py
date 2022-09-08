"""Search Entrypoint."""
from typing import List, Optional
from fastapi.routing import APIRouter
from fastapi.param_functions import Depends
from sqlalchemy.orm import Session

from core.dependencies import get_db
from core.schemas import BooksResponse
from core.db_operations import books_list

router = APIRouter(
    prefix="/books/search",
    tags=["search"],
)


@router.get("", response_model=BooksResponse)
def get_books(
    book_id: Optional[int] = None,
    language: Optional[str] = "",
    mime_type: Optional[str] = "",
    topic: Optional[str] = "",
    author: Optional[str] = "",
    title: Optional[str] = "",
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(get_db),
):
    filters = {
        "gutenberg_id": book_id,
        "language": list(map(str.lower, language.split(","))) if language else [],
        "mime_type": list(map(str.lower, mime_type.split(","))) if mime_type else [],
        "topic": list(map(str.lower, topic.split(","))) if topic else [],
        "author": list(map(str.lower, author.split(","))) if author else [],
        "title": list(map(str.lower, title.split(","))) if title else [],
    }
    count, books = books_list(db_session, filters, offset, limit)
    return {"no_of_books": count, "books": books}
