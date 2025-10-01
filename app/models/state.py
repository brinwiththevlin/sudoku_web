"""Puzzle State database model."""

from sqlalchemy import Column, PrimaryKeyConstraint, String
from sqlalchemy.schema import ForeignKey
from sqlalchemy.types import UUID

# Corrected the typo from base_clase to base_class
from app.db.base_class import Base


class PuzzleState(Base):
    """Represents the saved state of a puzzle for a specific user.

    This acts as a "join table" between users and puzzles.
    """

    __tablename__ = "puzzle_states"  # Use a more descriptive, plural name

    # Foreign key to the 'users' table
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True)

    # Foreign key to the 'puzzles' table
    puzzle_id = Column(UUID(as_uuid=True), ForeignKey("puzzles.id"), primary_key=True)

    # The actual state of the board as a string
    board = Column(String, nullable=False)

    # Define a composite primary key
    __table_args__ = (PrimaryKeyConstraint("user_id", "puzzle_id"),)
