import ormar

from typing import Optional

from app.core.db import database, metadata
from .user import User


class C2C(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "c2c"

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=128)
    description: str = ormar.String(max_length=512)
    cost: int = ormar.Integer()
    is_rented: bool = ormar.Boolean(default=False)
    users: Optional[User] = ormar.ForeignKey(User, nullable=True)
    
    # owner_name: str = ormar.String(max_length=32)
    # phone_number: str = ormar.String(max_length=)

