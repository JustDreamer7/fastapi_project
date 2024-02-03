import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Computed, Date, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.db import Base

if TYPE_CHECKING:
    from app.hotels.rooms.models import Rooms

class Bookings(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    date_from: Mapped[datetime.date] = mapped_column(Date)
    date_to: Mapped[datetime.date] = mapped_column(Date)
    price: Mapped[int]
    total_cost: Mapped[int] = mapped_column(Computed("(date_to - date_from) * price"))
    total_days: Mapped[int] = mapped_column(Computed("date_to - date_from"))

    room: Mapped["Rooms"] = relationship(back_populates="bookings")