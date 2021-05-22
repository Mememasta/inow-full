import ormar

from pydantic import EmailStr
from typing import Optional

from app.core.db import database, metadata
# from .c2c import C2C


class User(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "users"

    id: int = ormar.Integer(primary_key=True)
    # rent_id: Optional[int] = ormar.ForeignKey(C2C, nullable=True)
    email: EmailStr = ormar.String(max_length=256)
    phone_number: str = ormar.String(max_length=16)
    first_name: str = ormar.String(max_length=32)
    second_name: str = ormar.String(max_length=32)
    hashed_password: str = ormar.String(max_length=256)
    is_superuser: bool = ormar.Boolean(default=False)
    is_active: bool = ormar.Boolean(default=False)

