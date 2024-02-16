from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from contextlib import asynccontextmanager
from redis import asyncio as aioredis
from sqladmin import Admin

from app.admin.views import UsersAdmin, HotelsAdmin, RoomsAdmin, BookingsAdmin
from app.db import engine
from app.users.router import router as router_users
from app.bookings.router import router as router_bookings

from app.pages.router import router as router_pages
from app.images.router import router as router_images
from app.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = aioredis.from_url(f"redis://{settings.REDIS_HOST}", encoding='utf-8', decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="cache")
    yield


app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_pages)
app.include_router(router_images)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers",
                   "Access-Control-Allow-Origin",
                   "Authorization"],
)

admin = Admin(app, engine)
admin.add_view(UsersAdmin)
admin.add_view(HotelsAdmin)
admin.add_view(RoomsAdmin)
admin.add_view(BookingsAdmin)

app.mount("/static", StaticFiles(directory="app/static"), "static")

if __name__ == "__main__":
    import uvicorn

    import os.path
    import sys
    sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
    uvicorn.run(
        app="app.main:app",
        reload=True,
    )