from typing import TYPE_CHECKING

from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.db import Base

if TYPE_CHECKING:
    from app.bookings.models import Bookings
class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    hashed_password: Mapped[str]

    bookings: Mapped[list["Bookings"]] = relationship(back_populates="user")
    def __str__(self):
        return f"Пользователь {self.email}"