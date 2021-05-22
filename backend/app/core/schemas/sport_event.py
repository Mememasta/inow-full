import datetime

from typing import List, Optional
from pydantic import BaseModel

from app.core import models, schemas


class SportEventBase(BaseModel):
    name: str
    description: str
    event_date: datetime.datetime = datetime.datetime.utcnow()
    photo_path: str
    organizer: str
    checked: bool


class SportEventCreate(SportEventBase):
    pass


class SportEventUpdate(SportEventBase):
    pass


class SportEventSchema(SportEventBase):
    id: Optional[int]

    user: Optional[schemas.UserSchema]
    
    class Config:
        orm_mode = True
