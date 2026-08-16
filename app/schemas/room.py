from pydantic import BaseModel
from sqlmodel import SQLModel


# schemas/room.py file
# Note: Pydantic Schema = What data is allowed in or out of API

# Input Schema
# Note: Incoming data from user (i.e. not from db) therefore inherit from BaseModel b/c data already serialized.
# Note 2: SQLModel inherits from BaseModel. So can use SQLModel for everything where previously used BaseModel.
class RoomCreate(SQLModel):
    # Note omit id attribute from table model, to prevent overwrite existing room id
    name: str
    capacity: int
    location: str | None = None     # None --> Optional field


# Output Schema (i.e. Response Model)
# Note: Responding with object from database. Inherit from SQLModel to serialize db object to dict used by Pydantic.
class RoomPublic(SQLModel):
    id: int
    name: str
    capacity: int
    location: str | None = None




