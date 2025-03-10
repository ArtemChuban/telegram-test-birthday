from datetime import date

from app.auth import get_current_user
from app.models import Users
from app.schemas import UserSchema
from fastapi import APIRouter, Body, Depends, HTTPException, Path, status
from telegram_webapp_auth.data import WebAppUser

router = APIRouter(prefix="/users")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(
    user: WebAppUser = Depends(get_current_user),
    birthday: date = Body(embed=True),
) -> UserSchema:
    """
    Create a new user in the system based on the provided user information and birthday.

    This endpoint allows the creation of a new user if the user does not already exist in the database.
    It requires the authenticated user's information and their birthday. If a user with the same ID already exists,
    a 409 Conflict error is raised.
    """
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
    """
    Retrieve the authenticated user's information.

    This endpoint returns the details of the currently authenticated user.
    It uses the user's ID to fetch their information from the database.
    If the user is not found, a 404 Not Found error is raised.
    """
    instance = await Users.get_or_none(id=user.id)
    if instance is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return await UserSchema.from_tortoise_orm(instance)


@router.get("/{user_id}")
async def get_user(
    user_id: int = Path(),
) -> UserSchema:
    """
    Retrieve a user's information by their user ID.

    This endpoint fetches the details of a user specified by the user ID in the path parameter.
    If the user is not found in the database, a 404 Not Found error is raised.
    """
    instance = await Users.get_or_none(id=user_id)
    if instance is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return await UserSchema.from_tortoise_orm(instance)


@router.patch("/me")
async def update_birthday(
    user: WebAppUser = Depends(get_current_user),
    birthday: date = Body(embed=True),
) -> UserSchema:
    """
    Update the authenticated user's birthday.

    This endpoint allows the authenticated user to update their birthday.
    It retrieves the user's information from the database and updates the birthday field.
    If the user is not found, a 404 Not Found error is returned.
    """
    instance = await Users.get_or_none(id=user.id)
    if instance is None:
        return HTTPException(status.HTTP_404_NOT_FOUND)
    instance.birthday = birthday
    await instance.save()
    return await UserSchema.from_tortoise_orm(instance)
