from typing import List, Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    phone_number: int
    first_name: str
    second_name: str
    is_superuser: Optional[bool] = False
    is_active: Optional[bool] = False


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    password: str


class UserSchema(UserBase):
    id: Optional[int]

    class Config:
        orm_mode = True
