import datetime

from fastapi import APIRouter, Depends
from app.users.dependencies import get_current_user
from app.exceptions import RoomCannotBeBooked
from app.bookings.repo import BookingsRepo
from app.users.models import Users
from app.bookings.schemas import SBookings

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)):  # -> list[SBookings]:
    return await BookingsRepo.find_all(user_id=user.id)


@router.get("{booking_id}")
async def get_booking_by_id(booking_id: int) -> SBookings:
    return await BookingsRepo().find_by_id(booking_id)


@router.post("")
async def add_booking(room_id: int, date_from: datetime.date, date_to: datetime.date,
                      user: Users = Depends(get_current_user)):
    booking = await BookingsRepo().add(user.id, room_id, date_from, date_to)
    if not booking:
        raise RoomCannotBeBooked