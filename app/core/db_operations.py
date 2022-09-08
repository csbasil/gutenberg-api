from sqlalchemy.sql import func, text
from sqlalchemy import nullslast, or_, and_, any_
from sqlalchemy.orm import joinedload

from core.models import ( 
    Book, 
    Author,
    Subject,
    Language, 
    Shelf,
    Format,
    BookLanguage, 
    BookAuthor,
    BookShelf,
    BookSubject
)
    
    


def books_list(database, filters: dict = None, offset: int = 0, limit: int = 25):
    if filters is None:
        filters = {}

    q = (database.query(Book)
        .options(joinedload(Book.languages), joinedload(Book.subjects), joinedload(Book.shelfs), joinedload(Book.authors))
    )
    c = (database.query(func.count(Book.id).over().label("no_of_books"))
        .options(joinedload(Book.languages), joinedload(Book.subjects), joinedload(Book.shelfs), joinedload(Book.authors))
    )
    filter_string = []
    if filters['gutenberg_id']:
        filter_string.append(Book.gutenberg_id == filters['gutenberg_id'])

    if filters['language']:
        lang_string = []
        for lang in filters['language']:
            lang_string.append(Book.languages.any(Language.code.match(lang)))
        filter_string.append(or_(*lang_string))
    
    if filters['mime_type']:
        mime_string = []
        for mime in filters['mime_type']:
            mime_string.append(Format.mime_type.match(mime))
        filter_string.append(or_(*mime_string))

    if filters['topic']:
        topic_string = []
        for topic in filters['topic']:
            topic_string.append(Book.subjects.any(Subject.name.match(topic)))
            topic_string.append(Book.shelfs.any(Shelf.name.match(topic)))
        filter_string.append(or_(*topic_string))

    if filters['title']:
        title_string = []
        for title in filters['title']:
            title_string.append(Book.title.match(title))
        filter_string.append(or_(*title_string))  

    if filters['author']:
        author_string = []
        for author in filters['author']:
            author_string.append(Book.authors.any(Author.name.match(author)))
        filter_string.append(or_(*author_string))    

    q = q.filter(and_(*filter_string)).order_by(nullslast(Book.download_count.desc()))

    count = q.count()
    books = q.offset(offset*limit).limit(limit).all()

    print(count)

    return count, books