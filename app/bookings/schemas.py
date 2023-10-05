from pydantic import BaseModel
import datetime


class SBookings(BaseModel):
    id: int
    room_id: int
    user_id: int
    date_from: datetime.date
    date_to: datetime.date
    price: int
    total_cost: int
    total_days: int

    # class Config: # в pydantic = "^2.1.1" необходимости в  class Config: orm_mode = True - нет.
    #     orm_mode = True