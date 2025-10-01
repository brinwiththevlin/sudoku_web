"""API routes for handling puzzle states and interactions."""

from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# Import CRUD functions and DB session (we'll need these to implement the logic)
from app.db.session import SessionLocal

# Import the Pydantic schemas you created
from app.schemas import puzzle_state as puzzle_state_schema

# Create an APIRouter instance
router = APIRouter()


# Dependency to get a database session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# This function directly translates your YAML spec for POST /state/{pid}
@router.post("/state/{puzzle_id}", summary="Save a puzzle state")
def save_puzzle_state(
    puzzle_id: UUID,  # This is the {pid} from the path
    user_id: UUID,  # This is the user_id from the query parameters
    state: puzzle_state_schema.PuzzleState,  # This is the request body
    db: Annotated[Session, Depends(get_db)],
) -> dict[str, str]:
    raise NotImplementedError


@router.get("/state/{puzzle_id}", summary="Retireve the puzzle state for a specific user")
def get_puzzle_state(
    puzzle_id: UUID,
    user_id: UUID,
    db: Annotated[Session, Depends(get_db)],
) -> dict[str, str]:
    raise NotImplementedError
