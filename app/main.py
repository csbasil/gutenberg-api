"""API Main Entry Point."""
from fastapi import FastAPI
from core.database import verify_postgres
from v1.endpoints import router as search_router

app = FastAPI()
app.add_event_handler("startup", verify_postgres)

app.include_router(search_router)


@app.get("/")
def root():
    """Test Root route"""
    return "Hello"
