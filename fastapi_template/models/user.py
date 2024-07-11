from typing import Optional

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    """Represents a user in the system."""

    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, nullable=False)
    username: str = Field(unique=True, nullable=False)
    password: str

    class Config:
        extra = "allow"
