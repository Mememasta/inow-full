import datetime

from typing import List, Optional
from pydantic import BaseModel

from app.core import models, schemas


class SportEventBase(BaseModel):
    name: str
    description: str
    event_date: datetime.datetime = datetime.datetime.now()
    photo_path: str
    checked: bool = False


class SportEventCreate(SportEventBase):
    pass


class SportEventUpdate(SportEventBase):
    pass


class SportEventSchema(SportEventBase):
    id: Optional[int]

    members: List[schemas.UserSchema]
    organizer: Optional[schemas.UserSchema]
    
    class Config:
        orm_mode = True
