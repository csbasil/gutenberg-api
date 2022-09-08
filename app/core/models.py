"""ORM mapping for underlaying database tables."""
# coding: utf-8
# pylint: disable = import-error
from sqlalchemy import (
    CheckConstraint,
    Column,
    ForeignKey,
    Integer,
    SmallInteger,
    String,
    text,
    Table,
)
from sqlalchemy.orm import relationship  # pylint: disable = import-error
from core.database import Base

# association tables

BookAuthor = Table(
    "books_book_authors",
    Base.metadata,
    Column(
        "id",
        Integer,
        primary_key=True,
        server_default=text("nextval('books_book_languages_id_seq'::regclass)"),
    ),
    Column(
        "author_id",
        ForeignKey("books_author.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    ),
    Column(
        "book_id",
        ForeignKey("books_book.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    ),
)

BookLanguage = Table(
    "books_book_languages",
    Base.metadata,
    Column(
        "id",
        Integer,
        primary_key=True,
        server_default=text("nextval('books_book_languages_id_seq'::regclass)"),
    ),
    Column(
        "language_id",
        ForeignKey("books_language.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    ),
    Column(
        "book_id",
        ForeignKey("books_book.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    ),
)
BookSubject = Table(
    "books_book_subjects",
    Base.metadata,
    Column(
        "id",
        Integer,
        primary_key=True,
        server_default=text("nextval('books_book_languages_id_seq'::regclass)"),
    ),
    Column(
        "subject_id",
        ForeignKey("books_subject.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    ),
    Column(
        "book_id",
        ForeignKey("books_book.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    ),
)

BookShelf = Table(
    "books_book_bookshelves",
    Base.metadata,
    Column(
        "id",
        Integer,
        primary_key=True,
        server_default=text("nextval('books_book_languages_id_seq'::regclass)"),
    ),
    Column(
        "bookshelf_id",
        ForeignKey("books_bookshelf.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    ),
    Column(
        "book_id",
        ForeignKey("books_book.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    ),
)

# tables


class Book(Base):
    """Book table."""

    __tablename__ = "books_book"
    __table_args__ = (
        CheckConstraint("download_count >= 0"),
        CheckConstraint("gutenberg_id >= 0"),
    )

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('books_book_id_seq'::regclass)"),
    )
    download_count = Column(Integer)
    gutenberg_id = Column(Integer, nullable=False, unique=True)
    media_type = Column(String(16), nullable=False)
    title = Column(String(1024))

    authors = relationship("Author", secondary=BookAuthor)
    languages = relationship("Language", secondary=BookLanguage)
    subjects = relationship("Subject", secondary=BookSubject)
    shelfs = relationship("Shelf", secondary=BookShelf)


class Author(Base):
    """Author table."""

    __tablename__ = "books_author"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('books_author_id_seq'::regclass)"),
    )
    birth_year = Column(SmallInteger)
    death_year = Column(SmallInteger)
    name = Column(String(128), nullable=False)


class Shelf(Base):
    """Shelf Table."""

    __tablename__ = "books_bookshelf"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('books_bookshelf_id_seq'::regclass)"),
    )
    name = Column(String(64), nullable=False, unique=True)


class Language(Base):
    """Language Table."""

    __tablename__ = "books_language"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('books_language_id_seq'::regclass)"),
    )
    code = Column(String(4), nullable=False, unique=True)


class Subject(Base):
    """Subject Table."""

    __tablename__ = "books_subject"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('books_subject_id_seq'::regclass)"),
    )
    name = Column(String(256), nullable=False)


class Format(Base):
    """Book Format Table."""

    __tablename__ = "books_format"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('books_format_id_seq'::regclass)"),
    )
    mime_type = Column(String(32), nullable=False)
    url = Column(String(256), nullable=False)
    book_id = Column(
        ForeignKey("books_book.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )

    book = relationship("Book", backref="formats", lazy="joined")
