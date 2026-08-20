from fastapi import APIRouter, HTTPException    # HTTPException used for returning graceful conflict message
from sqlmodel import select
from sqlalchemy.exc import IntegrityError

from app.schemas.reservation import ReservationCreate, ReservationPublic
from app.database import SessionDep
from app.models.reservation import Reservation

# Prefix in router so don't need to list "/reservations/xyz" for each endpoint
# The prefix lives inside the APIRouter( )
router = APIRouter(prefix="/reservations", tags=["reservations"])

# Create Reservation / POST
@router.post("", response_model=ReservationPublic, status_code=201)
def create_reservation(reservation: ReservationCreate, session: SessionDep): # Input param reservation: Type Res_Create
    # Turns inbound ReservationCreate obj into type Reservation object
    temp_reservation = Reservation.model_validate(reservation)
    session.add(temp_reservation)
    try:
        session.commit()
    except IntegrityError:                             # For returning graceful conflict message
        session.rollback()              # Session commit failed, so need to roll back to previous state
        raise HTTPException(status_code=409, detail="This room is already booked for that time.")
    session.refresh(temp_reservation)
    return temp_reservation


# List / Read / GET ALL Reservations
@router.get("", response_model=list[ReservationPublic])
def get_all_reservations(session: SessionDep):
    reservation_list = session.exec(select(Reservation)).all()
    return reservation_list


# Read / GET a specific reservation
@router.get("/{id}", response_model=ReservationPublic)
def get_reservation(id: int, session: SessionDep):
    requested_reservation = session.get(Reservation, id) # Avoids manual SQL "select()". Get Reservation table & id #.
    if requested_reservation is None:
        raise HTTPException(status_code=404, detail="Reservation id not found")
    return requested_reservation

# DELETE a reservation
@router.delete("/{id}", status_code=204)      # There is nothing returned --> No return type & 204 response
def delete_reservation(id: int, session: SessionDep):
    temp_reservation = session.get(Reservation, id)
    if temp_reservation is None:
        raise HTTPException(status_code=404, detail="Reservation id not found")
    session.delete(temp_reservation)
    session.commit()

