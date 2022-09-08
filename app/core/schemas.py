from typing import List, Optional
from pydantic import BaseModel


class BookAuthor(BaseModel):
    name: str
    birth_year: Optional[int]
    death_year: Optional[int]

    class Config:
        orm_mode = True


class BookShelf(BaseModel):
    name: str

    class Config:
        orm_mode = True


class BookLanguage(BaseModel):
    code: str

    class Config:
        orm_mode = True


class BookSubject(BaseModel):
    name: str

    class Config:
        orm_mode = True


class BookFormat(BaseModel):
    mime_type: str
    url: str

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    title: Optional[str]
    authors: Optional[List[BookAuthor]]
    languages: Optional[List[BookLanguage]]
    subjects: Optional[List[BookSubject]]
    shelfs: Optional[List[BookShelf]]
    formats: Optional[List[BookFormat]]

    class Config:
        orm_mode = True


class BooksResponse(BaseModel):
    no_of_books: int
    books: List[BookBase]

    class Config:
        orm_mode = True
