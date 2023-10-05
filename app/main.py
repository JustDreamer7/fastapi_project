from fastapi import FastAPI
from dataclasses import dataclass, asdict
import datetime
from typing import Union, Optional, List

from app.fake_data import Pet, PetFactory
from app.users.router import router as router_users
from app.bookings.router import router as router_bookings

app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)
pets_res = [PetFactory.build() for item in range(20)]

@dataclass
class PetArgs:
    name: str
    age: int
    type: Optional[str]
    created_at: Optional[datetime.datetime]

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("hotels")
def read_item(limit: Optional[int] = 20) -> dict:
    return {"count": len(pets_res[:limit]), 'items': pets_res[:limit]}

@app.get("hotels/{pets_id}")
def read_item(pets_id: int) -> Pet:
    return pets_res[pets_id]


@app.put("hotels")
def update_item(pet: PetArgs):
    _id = next(PetFactory.id_iter)
    res = {"id": _id}
    res.update(asdict(pet))
    pets_res.append(res)
    return res


@app.delete("hotels")
def update_item(item_id: int, item: Pet):
    return {"item_name": item.name, "item_id": item_id}
