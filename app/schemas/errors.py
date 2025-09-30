"""Pydantic class for erorr object."""

from pydantic import BaseModel


class APIError(BaseModel):
    """Defines the standard error response format for the API."""

    code: str
    message: str
