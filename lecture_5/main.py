from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .models import Book
from .schemas import BookIn, BookOut

# Creates all tables if they don't exist.
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Lecture 5 - Book API")


@app.post("/books/", response_model=BookOut)
def create_book(data: BookIn, db: Session = Depends(get_db)):
    """
    Insert a new book into the database.
    """
    item = Book(**data.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@app.get("/books/", response_model=list[BookOut])
def get_all(db: Session = Depends(get_db)):
    """
    Return all books from the table.
    """
    return db.query(Book).all()


@app.get("/books/{book_id}", response_model=BookOut)
def get_one(book_id: int, db: Session = Depends(get_db)):
    """
    Get a single book by its ID. If no book - 404 error
    """
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(404, "Book not found")
    return book


@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """
    Delete a book by ID.
    """
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(404, "Book not found")

    db.delete(book)
    db.commit()
    return {"status": "deleted"}


@app.put("/books/{book_id}", response_model=BookOut)
def update_book(book_id: int, data: BookIn, db: Session = Depends(get_db)):
    """
    Replace book data with new values.
    """
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(404, "Book not found")

    for field, value in data.dict().items():
        setattr(book, field, value)

    db.commit()
    db.refresh(book)
    return book


@app.get("/books/search/", response_model=list[BookOut])
def search_books(q: str, db: Session = Depends(get_db)):
    """
    search by title, author, or year.
    """
    results = db.query(Book).filter(
        (Book.title.ilike(f"%{q}%")) |
        (Book.author.ilike(f"%{q}%"))
    ).all()

    if q.isdigit():
        year_matches = db.query(Book).filter(Book.year == int(q)).all()
        for b in year_matches:
            if b not in results:
                results.append(b)

    return results
