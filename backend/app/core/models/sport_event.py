from typing import List, Optional
import ormar
import datetime

from app.core.db import database, metadata
from .user import User


class SportEvent(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "sportevent"

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=128)
    description: str = ormar.String(max_length=512)
    event_date: datetime.datetime = ormar.DateTime(default=datetime.datetime.utcnow)
    photo_path: str = ormar.String(max_length=1024)
    checked: bool = ormar.Boolean(default=False)


    members: List[User] = ormar.ForeignKey(User, related_name="members", nullable=True)
    organizer: Optional[User] = ormar.ForeignKey(User, related_name="organizer", nullable=True)
