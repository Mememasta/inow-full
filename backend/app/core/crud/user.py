from fastapi.encoders import jsonable_encoder
from typing import Any, Dict, Optional, Union

from pydantic.networks import EmailStr

from app.core.security import get_password_hash, verify_password
from app.core.crud.base import CRUDBase
from app.core.models.user import User
from app.core.schemas.user import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    async def get_by_email(self, *, email: str) -> Optional[User]:
        return await self.model.objects.get_or_none(email=email)

    async def create(self, *, schema: UserCreate) -> User:
        db_obj = User(
            email=schema.email,
            phone_number=schema.phone_number,
            first_name=schema.first_name,
            second_name=schema.second_name,
            hashed_password=await get_password_hash(schema.password),
            is_active=schema.is_active,
            is_superuser=schema.is_superuser
        )
        obj_in_data = jsonable_encoder(db_obj)
        return await self.model(**obj_in_data).save()

    async def update(self, id: int, *, schema: Union[UserUpdate, Dict[str, Any]]) -> Optional[User]:
        if isinstance(schema, dict):
            update_data = schema
        else:
            update_data = schema.dict(exclude_unset=True)
        if update_data["password"]:
            hashed_password = await get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return await super().update(id=id, schema=update_data)

    async def is_active(self, user: User) -> bool:
        return user.is_active

    async def is_superuser(self, user: User) -> bool:
        return user.is_superuser

    async def authenticate(self, *, email: EmailStr, password: str) -> Optional[User]:
        user = await self.get_by_email(email=email)
        if not user:
            return None
        if not await verify_password(password, user.hashed_password):
            return None
        return user


user = CRUDUser(User)
