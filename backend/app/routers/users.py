from datetime import date

from app.auth import get_current_user
from app.models import Users
from app.schemas import UserSchema
from fastapi import APIRouter, Body, Depends, HTTPException, Path, status
from telegram_webapp_auth.data import WebAppUser

router = APIRouter(prefix="/users")


@router.post("/")
async def create_user(
    user: WebAppUser = Depends(get_current_user),
    birthday: date = Body(embed=True),
) -> UserSchema:
    exist = await Users.exists(id=user.id)
    if exist:
        raise HTTPException(status.HTTP_409_CONFLICT)
    instance = await Users.create(
        id=user.id,
        first_name=user.first_name,
        last_name=user.last_name,
        username=user.username,
        birthday=birthday,
    )
    return UserSchema(
        id=instance.id,
        first_name=instance.first_name,
        last_name=instance.last_name,
        username=instance.username,
        birthday=instance.birthday,
    )


@router.get("/me")
async def get_me(
    user: WebAppUser = Depends(get_current_user),
) -> UserSchema:
    instance = await Users.get_or_none(id=user.id)
    if instance is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return UserSchema(
        id=instance.id,
        first_name=instance.first_name,
        last_name=instance.last_name,
        username=instance.username,
        birthday=instance.birthday,
    )


@router.get("/{user_id}")
async def get_user(
    user_id: int = Path(),
) -> UserSchema:
    instance = await Users.get_or_none(id=user_id)
    if instance is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return UserSchema(
        id=instance.id,
        first_name=instance.first_name,
        last_name=instance.last_name,
        username=instance.username,
        birthday=instance.birthday,
    )
