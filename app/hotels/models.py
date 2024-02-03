from typing import TYPE_CHECKING

from sqlalchemy import JSON, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.db import Base

if TYPE_CHECKING:
    from app.hotels.rooms.models import Rooms

class Hotels(Base):
    __tablename__ = "hotels"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str]
    location: Mapped[str]
    services: Mapped[list[str]] = mapped_column(JSON)
    rooms_quantity: Mapped[int]
    image_id: Mapped[int]

    rooms: Mapped[list["Rooms"]] = relationship(back_populates="hotel")