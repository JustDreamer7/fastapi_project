from pydantic import BaseModel, ConfigDict
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

    model_config = ConfigDict(from_attributes=True)
    # class Config: # в pydantic = "^2.1.1" необходимости в  class Config: orm_mode = True - нет.
    #     orm_mode = True

class SNewBooking(BaseModel):
    room_id: int
    date_from: datetime.date
    date_to: datetime.date