from sqlalchemy import select

from app.repo.base import BaseRepo
from app.bookings.models import Bookings
from app.db import async_session_maker

class BookingsRepo(BaseRepo):
    # model = Bookings.__table__.columns
    model = Bookings