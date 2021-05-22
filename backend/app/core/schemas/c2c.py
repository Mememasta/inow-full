from typing import List, Optional
from pydantic import BaseModel

from app.core import models, schemas


class C2CBase(BaseModel):
    name: str
    description: str
    cost: int
    is_rented: bool = False


class C2CCreate(C2CBase):
    pass


class C2CUpdate(C2CBase):
    pass


class C2CSchema(C2CBase):
    id: Optional[int]
    users: Optional[schemas.UserSchema]

    class Config:
        orm_mode = True
