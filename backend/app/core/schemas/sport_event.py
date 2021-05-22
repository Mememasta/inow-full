import datetime

from typing import List, Optional
from pydantic import BaseModel


class SportEventBase(BaseModel):
    name: str
    description: str
    event_date: datetime.datetime
    photo_path: str
    organizer: str


class SportEventCreate(SportEventBase):
    pass


class SportEventUpdate(SportEventBase):
    pass


class SportEventSchema(SportEventBase):
    id: Optional[int]

    class Config:
        orm_mode = True
