"""puzzle database calss, different from the json class."""

import uuid

from sqlalchemy import Column, String
from sqlalchemy.types import UUID

from app.db.base_class import Base


class Puzzle(Base):
    """Class representing the Puzzle table.

    Attributes:
        __tablename__ (str): tabel bane
        id (Column[UUID]): puzzle id
        puzzle_name (Column[String]): name of the puzzle
        board (Column[String]): serialized version of the puzzle state
    """

    __tablename__ = "puzzle"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    puzzle_name = Column(String, unique=True, index=True, nullable=False)
    board = Column(String, nullable=False)
