from pygments.lexer import default
from sqlmodel import SQLModel, Field


# SQLModel used to convert returned db objects into serialized (flat) data Pydantic can use

class User(SQLModel, table=True):       #table=True --> Maps to db table
    id: int | None = Field(default=None, primary_key=True)
    full_name: str
    email: str

