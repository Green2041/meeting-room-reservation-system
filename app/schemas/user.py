from pydantic import BaseModel
from sqlmodel import SQLModel


# Incoming Data Schema
class UserCreate(BaseModel):    #Arg type BaseModel b/c incoming data is flat serialized json or dict.
    full_name: str
    email: str

# Outgoing Data Schema
class UserPublic(SQLModel):    #Returns object from db. Needs SQLModel type arg to accept. Then flattens for pydantic
    id: int
    full_name: str
    email: str
