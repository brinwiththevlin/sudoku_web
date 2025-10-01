"""Connection handler."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# The path to your SQLite database file
SQLALCHEMY_DATABASE_URL = "sqlite:///./identifier.sqlite"

engine = create_engine(
    # `check_same_thread` is only needed for SQLite
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

# Each instance of SessionLocal will be a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
