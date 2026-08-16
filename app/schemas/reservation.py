# app/schemas/reservation.py
from pydantic import BaseModel
from sqlmodel import SQLModel
from datetime import datetime


# Input Schema
class ReservationCreate(BaseModel):
    room_id: int
    user_id: int
    start_time: datetime
    end_time: datetime
    title: str | None=None  # Optional

# Return Output Schema
class ReservationPublic(SQLModel):
    id: int
    room_id: int
    user_id: int
    start_time: datetime
    end_time: datetime
    created_at: datetime
    title: str | None=None  # Optional