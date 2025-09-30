"""Pydantic class for PuzzleState object."""

from typing import Annotated

from pydantic import BaseModel, Field


class PuzzleState(BaseModel):
    """Represents the state of a Sudoku puzzle grid."""

    grid: Annotated[str, Field(min_length=81, max_length=81)]
