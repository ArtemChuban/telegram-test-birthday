from typing import TypeAlias

from tortoise.contrib.pydantic import pydantic_model_creator

from app.models import Users

UserSchema: TypeAlias = pydantic_model_creator(Users)  # type: ignore[valid-type] # mypy interprets the type incorrectly
