from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from dataclasses import dataclass, asdict
import datetime
from typing import Union, Optional, List

from app.users.router import router as router_users
from app.bookings.router import router as router_bookings

from app.pages.router import router as router_pages
from app.images.router import router as router_images
app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_pages)
app.include_router(router_images)

@dataclass
class PetArgs:
    name: str
    age: int
    type: Optional[str]
    created_at: Optional[datetime.datetime]

@app.get("/")
def read_root():
    return {"Hello": "World"}
