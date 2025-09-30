"""Pydantic specs for the User datatable."""

# app/schemas/user.py
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """Shared base properties for a User.

    This class defines the common attributes that are present in all user-related schemas.
    """

    email: EmailStr


class UserCreate(UserBase):
    """Properties to receive via API on user creation.

    This model is used when a new user signs up. It inherits the email field
    from UserBase and can be extended with other fields like a password.
    """

    # For now, creating a user just requires an email


class User(UserBase):
    """Properties to return to a client.

    This model represents a user as it is returned from the API. It includes
    the user's database ID and username, but sensitive information like a
    password hash would be excluded here.
    """

    id: int
    username: str

    class Config:
        """Pydantic configuration settings for the User model."""

        # This allows the model to be created from ORM objects (e.g., SQLAlchemy models)
        # It tells Pydantic to read the data even if it is not a dict, but an ORM model.
        from_attributes = True
