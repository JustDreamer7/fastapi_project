from sqlalchemy.orm import mapped_column, Mapped
from app.db import Base


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    hashed_password: Mapped[str]

    def __str__(self):
        return f"Пользователь {self.email}"