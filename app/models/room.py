from sqlmodel import Field, SQLModel
# models/room.py file
# Note: Tabel model = Shape of the data in the database table

class Room(SQLModel,table=True):        # table=True tells SQLModel this is a table model (i.e., table fields/columns)
    # Sets id as table primary key. Will automatically assign id#.
    id: int | None = Field(default=None, primary_key=True)
    name: str
    capacity: int
    location: str | None = None

