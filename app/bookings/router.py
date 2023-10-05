from fastapi import APIRouter, Depends
from app.users.dependencies import get_current_user

from app.bookings.repo import BookingsRepo
from app.users.models import Users
from app.bookings.schemas import SBookings

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)):  # -> list[SBookings]:
    return await BookingsRepo.find_all(user_id=1)
    # return await BookingsRepo().find_all()


@router.get("{booking_id}")
async def get_booking_by_id(booking_id: int) -> SBookings:
    return await BookingsRepo().find_by_id(booking_id)

# @router.get("")
# async def get_bookings() -> SBookings:
#     return await BookingsRepo().find_one_or_none(room_id=1)
