"""Pydantic schemas for request/response models."""
from typing import List, Optional
from pydantic import BaseModel


class BookAuthor(BaseModel):
    """Book author schema."""

    name: str
    birth_year: Optional[int]
    death_year: Optional[int]

    class Config:
        orm_mode = True


class BookShelf(BaseModel):
    """Book shelf schema."""

    name: str

    class Config:
        orm_mode = True


class BookLanguage(BaseModel):
    """Book language schema."""

    code: str

    class Config:
        orm_mode = True


class BookSubject(BaseModel):
    """Book subject schema."""

    name: str

    class Config:
        orm_mode = True


class BookFormat(BaseModel):
    """Book format schema."""

    mime_type: str
    url: str

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    """Book Base schema."""

    title: Optional[str]
    authors: Optional[List[BookAuthor]]
    languages: Optional[List[BookLanguage]]
    subjects: Optional[List[BookSubject]]
    shelfs: Optional[List[BookShelf]]
    formats: Optional[List[BookFormat]]

    class Config:
        orm_mode = True


class BooksResponse(BaseModel):
    """Book Response schema."""

    no_of_books: int
    books: List[BookBase]

    class Config:
        orm_mode = True
