import datetime

from fastapi import APIRouter, Depends
from pydantic import TypeAdapter

from app.tasks.tasks import send_booking_confirmation_email
from app.users.dependencies import get_current_user
from app.exceptions import RoomCannotBeBooked
from app.bookings.repo import BookingsRepo
from app.users.models import Users
from app.bookings.schemas import SBookings, SNewBooking

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
async def add_booking(booking: SNewBooking,
                      user: Users = Depends(get_current_user)):
    booking = await BookingsRepo().add(user.id, booking.room_id,
                                       booking.date_from,
                                       booking.date_to)
    if not booking:
        raise RoomCannotBeBooked
    # В новой версии pydantic необходимо использовать TypeAdapter, он парсит данные из booking по SNewBooking
    booking = TypeAdapter(SNewBooking).validate_python(booking).model_dump()
    send_booking_confirmation_email(booking, user.email)
    return booking
