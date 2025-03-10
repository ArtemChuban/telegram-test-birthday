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
    if await Users.exists(id=user.id):
        raise HTTPException(status.HTTP_409_CONFLICT)
    instance = await Users.create(
        id=user.id,
        first_name=user.first_name,
        last_name=user.last_name,
        username=user.username,
        birthday=birthday,
    )
    return await UserSchema.from_tortoise_orm(instance)


@router.get("/me")
async def get_me(
    user: WebAppUser = Depends(get_current_user),
) -> UserSchema:
    instance = await Users.get_or_none(id=user.id)
    if instance is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return await UserSchema.from_tortoise_orm(instance)


@router.get("/{user_id}")
async def get_user(
    user_id: int = Path(),
) -> UserSchema:
    instance = await Users.get_or_none(id=user_id)
    if instance is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return await UserSchema.from_tortoise_orm(instance)


@router.patch("/me")
async def update_birthday(
    user: WebAppUser = Depends(get_current_user),
    birthday: date = Body(embed=True),
) -> UserSchema:
    instance = await Users.get_or_none(id=user.id)
    if instance is None:
        return HTTPException(status.HTTP_404_NOT_FOUND)
    instance.birthday = birthday
    await instance.save()
    return await UserSchema.from_tortoise_orm(instance)
