from tortoise import fields, models


class Users(models.Model):
    id = fields.BigIntField(primary_key=True)
    first_name = fields.CharField(max_length=255)
    last_name = fields.CharField(max_length=255, null=True)
    username = fields.CharField(max_length=255, null=True)
    birthday = fields.DateField()
