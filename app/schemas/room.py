from pydantic import BaseModel
from sqlmodel import SQLModel


# schemas/room.py file
# Note: Pydantic Schema = What data is allowed in or out of API

# Input Model
class RoomCreate(BaseModel):
    # Note omit id attribute from table model, to prevent overwrite existing room id
    name: str
    capacity: int
    location: str | None = None     # None --> Optional field


# Output Model (i.e. Response Model)
# Note: Responding with object from database. Inherit from SQLModel to serialize db object to dict used by Pydantic.
class RoomPublic(SQLModel):
    id: int
    name: str
    capacity: int
    location: str | None = None




