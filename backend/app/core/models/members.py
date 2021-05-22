import ormar

from typing import Optional, List

from app.core.db import database, metadata
from .user import User
from .sport_event import SportEvent


class Members(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "members"

    id: int = ormar.Integer(primary_key=True)

    # user: Optional[User] = ormar.ForeignKey(User, virtual=False, nullable=True)
    users: Optional[List[User]] = ormar.ManyToMany(User)
    events: Optional[List[SportEvent]] = ormar.ManyToMany(SportEvent)
