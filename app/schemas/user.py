from sqlmodel import SQLModel


# Incoming Data Schema
#Arg type BaseModel b/c incoming data is flat serialized json or dict.
class UserCreate(SQLModel):     # Changed to SQLModel because inherits from BaseModel.
    full_name: str
    email: str

# Outgoing Data Schema
class UserPublic(SQLModel):    #Returns object from db. Needs SQLModel type arg to accept. Then flattens for pydantic
    id: int
    full_name: str
    email: str
