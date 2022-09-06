"""Search Entrypoint."""
from fastapi.routing import APIRouter

router = APIRouter(
    prefix="/books/search",
    tags=["search"],
)
