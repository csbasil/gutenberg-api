"""Perform Operations on database from ORM layer."""
from sqlalchemy import nullslast, or_, and_  # pylint: disable = import-error
from sqlalchemy.orm import joinedload  # pylint: disable = import-error

from core.models import Book, Author, Subject, Language, Shelf, Format


def books_list(database, filters: dict = None, offset: int = 0, limit: int = 25):
    """Get list of books based on filters."""

    if filters is None:
        filters = {}

    book_query = database.query(Book).options(
        joinedload(Book.languages),
        joinedload(Book.subjects),
        joinedload(Book.shelfs),
        joinedload(Book.authors),
    )

    filter_string = []
    if filters["gutenberg_id"]:
        filter_string.append(Book.gutenberg_id == filters["gutenberg_id"])

    if filters["language"]:
        lang_string = []
        for lang in filters["language"]:
            lang_string.append(Book.languages.any(Language.code.match(lang)))
        filter_string.append(or_(*lang_string))

    if filters["mime_type"]:
        mime_string = []
        for mime in filters["mime_type"]:
            mime_string.append(Format.mime_type.match(mime))
        filter_string.append(or_(*mime_string))

    if filters["topic"]:
        topic_string = []
        for topic in filters["topic"]:
            topic_string.append(Book.subjects.any(Subject.name.match(topic)))
            topic_string.append(Book.shelfs.any(Shelf.name.match(topic)))
        filter_string.append(or_(*topic_string))

    if filters["title"]:
        title_string = []
        for title in filters["title"]:
            title_string.append(Book.title.match(title))
        filter_string.append(or_(*title_string))

    if filters["author"]:
        author_string = []
        for author in filters["author"]:
            author_string.append(Book.authors.any(Author.name.match(author)))
        filter_string.append(or_(*author_string))

    book_query = book_query.filter(and_(*filter_string)).order_by(
        nullslast(Book.download_count.desc())
    )

    count = book_query.count()
    books = book_query.offset(offset * limit).limit(limit).all()
    return count, books
