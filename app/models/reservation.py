# /app/models/reservation.py
from sqlmodel import SQLModel, Field
from datetime import datetime, timezone
from sqlalchemy import DateTime


class Reservation(SQLModel, table=True):
    id: int | None=Field(default=None, primary_key=True)    # None --> Will be assigned by SQL automatically. Also PK.
    room_id: int=Field(foreign_key="room.id")   # Get from the SQL db level. Not from room.py class. Pass in as str.
    user_id: int=Field(foreign_key="user.id")   # Get from the SQL db level. Not from user.py class. Pass in as str.
    start_time: datetime=Field(sa_type=DateTime(timezone=True)) #Tells SQL db to keep track of timezone for this var.
    end_time: datetime=Field(sa_type=DateTime(timezone=True))   #Tells SQL db to keep track of timezone for this var.
    # sa_type allows you to override SQLModel's automatic column type and specify to use a timezone aware column in db.
    title: str | None=None
    created_at: datetime=Field(
        # default_factory -> SQLModel calls each time a new row is created (i.e. not just once on startup)
        default_factory=lambda: datetime.now(timezone.utc),     # What time value to get and when to get it
        sa_type=DateTime(timezone=True))                        # How to store it as a time zone aware type




