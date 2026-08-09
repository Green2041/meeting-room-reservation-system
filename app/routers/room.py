from fastapi import APIRouter   # Needed to create router instance
from sqlmodel import select

from app.schemas.room import RoomCreate, RoomPublic
from app.database import SessionDep
from app.models.room import Room

# Prefix in router so don't need to list "/rooms/xyz" each time\
# The prefix lives inside the APIRouter( )
router = APIRouter(prefix="/rooms", tags=["rooms"])

# CREATE
@router.post("", response_model=RoomPublic)     # response_model --> What schema comes out
def create_room(room: RoomCreate, session : SessionDep):   # Input parameter room: Type RoomCreate --> What comes in
    temp_room = Room.model_validate(room)   # Turns incoming RoomCreate type object into type Room object
    session.add(temp_room)                  # Add the converted Room object to a session
    session.commit()                       # Commit any & all changes to the database
    session.refresh(temp_room)             # Updates temp_room in place; now with it's db assigned id
                                            # Need to pass in temp_room so refresh() knowns what table to refresh
    return temp_room                       # Return to user.


# List / return all rooms
@router.get("", response_model=list[RoomPublic])     # response_model --> Return list of RoomPublic type objects
def get_all_rooms(session: SessionDep):             # No input parameter. Still need session connection
    room_list = session.exec(select(Room)).all()           # Session connection runs SQL Query "SELECT * FROM rooms"
    return room_list



# Get / return a specific room
@router.get("/{id}", response_model=RoomPublic)     #Again return type RoomPublic
def get_room(id: int, session: SessionDep):              # Input parameter room id. Need session connection parameter
    room_requested = session.get(Room, id)               # session.get(Room, id) avoids manual SQL with "select()"
    return  room_requested



# Delete a room
@router.delete("/{id}")                             # There is nothing returned --> No return type
def delete_room(id: int, session: SessionDep):       # Need room id: type int as input arg. Need session connect to db
    temp_room = session.get(Room, id)
    session.delete(temp_room)
    session.commit()                          # Need to commit the deletion in local session connection to the db table
    return {"message": "No contents"}
