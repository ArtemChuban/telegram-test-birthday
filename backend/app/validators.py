from datetime import date

from tortoise.exceptions import ValidationError
from tortoise.validators import Validator


class PastDateValidator(Validator):
    def __call__(self, value: date) -> None:
        if value > date.today():
            raise ValidationError("Value must be in past")
