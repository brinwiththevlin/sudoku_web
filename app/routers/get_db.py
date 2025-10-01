"""Database getter."""

# Import CRUD functions and DB session (we'll need these to implement the logic)
from collections.abc import Generator

from sqlalchemy.orm import Session

from app.db.session import SessionLocal

# Import the Pydantic schemas you created


def get_db() -> Generator[Session]:
    """Returns the database."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
