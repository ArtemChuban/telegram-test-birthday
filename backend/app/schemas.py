from datetime import date

from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    first_name: str
    last_name: str | None
    username: str | None
    birthday: date
