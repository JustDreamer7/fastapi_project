from pydantic import BaseModel
from faker import Faker
import datetime
from typing import Optional
import itertools

fake = Faker()


class Pet(BaseModel):
    id: int
    name: str
    age: Optional[int]
    type: str
    created_at: Optional[datetime.datetime]


class PetFactory:
    id_iter = itertools.count()

    @classmethod
    def generate_name(cls):
        return Faker().name()

    @classmethod
    def generate_age(cls):
        return Faker().random_int(0, 15)

    @classmethod
    def generate_type(cls):
        # Поменять
        return Faker().company()

    @classmethod
    def generate_create_at(cls):
        return Faker().date_time_this_decade(before_now=True)

    @classmethod
    def build(cls):
        _id = next(PetFactory.id_iter)
        name = cls.generate_name()
        _type = cls.generate_type()
        age = cls.generate_age()
        created_at = cls.generate_create_at()

        return Pet(id=_id, name=name, age=age, type=_type, created_at=created_at)