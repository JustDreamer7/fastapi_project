import datetime

from sqlalchemy import select, func, insert

from app.repo.base import BaseRepo
from app.bookings.models import Bookings
from app.db import async_session_maker
from app.hotels.rooms.models import Rooms


class BookingsRepo(BaseRepo):
    # model = Bookings.__table__.columns
    model = Bookings

    @classmethod
    async def add(cls, user_id, room_id: int, date_from: datetime.date, date_to: datetime.date):
        async with async_session_maker() as session:
            booked_rooms = select(Bookings).where(
                (Bookings.room_id == 1) & (Bookings.date_from < date_to) & (Bookings.date_to > date_from)).cte(
                'booked_rooms')
            rooms_left = select(
                Rooms.quantity - func.count(booked_rooms.c.room_id).label('rooms_left')
            ).select_from(Rooms).join(booked_rooms, booked_rooms.c.room_id == Rooms.id, isouter=True
            ).where(Rooms.id == 1).group_by(Rooms.quantity, booked_rooms.c.room_id)
            rooms_left = await session.execute(rooms_left)
            rooms_left: int = rooms_left.scalar()
            if rooms_left > 0:
                get_price = select(Rooms.price).filter_by(id=room_id)
                price = await session.execute(get_price)
                price: int = price.scalar()
                add_bookings = insert(Bookings).values(
                    room_id=room_id,user_id=user_id,date_from=date_from,
                    date_to=date_to,price=price,).returning(Bookings)
                new_booking = await session.execute(add_bookings)
                return new_booking.scalar()
            else:
                return None