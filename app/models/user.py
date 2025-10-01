"""User databse calss, different from the json class."""

import uuid

from sqlalchemy import Column, String
from sqlalchemy.types import UUID

from app.db.base_class import Base


class User(Base):
    """Sqlalchemy class to represent the user tables.

    Attributes:
        __tablename__ (str): the table name
        id (Column[UUID]): the user_id
        username (Column[String]): the username of the user
        email
    """

    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
