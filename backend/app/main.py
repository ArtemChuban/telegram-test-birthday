from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from app.routers.users import router as users_router
from app.settings import TORTOISE_ORM_SETTINGS

app = FastAPI()
register_tortoise(app, TORTOISE_ORM_SETTINGS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(users_router)
