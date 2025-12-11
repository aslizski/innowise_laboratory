from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# lecture_5 folder path (
BASE_DIR = Path(__file__).parent.resolve()

# DB file
DB_URL = f"sqlite:///{BASE_DIR / 'books.db'}"

engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    """
    Returns a DB session for each request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
