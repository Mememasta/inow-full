from fastapi.encoders import jsonable_encoder
from typing import Any, Dict, Optional, Union

from app.core.crud.base import CRUDBase
from app.core import models, crud
from app.core.models.c2c import C2C
from app.core.schemas.c2c import C2CCreate, C2CUpdate


class CRUDUser(CRUDBase[C2C, C2CCreate, C2CUpdate]):
    async def get(self, id: int) -> Optional[C2C]:
        get_rent = await self.model.objects.select_related("user").get_or_none(pk=id)
        return get_rent

    async def get_multy(self) -> Optional[C2C]:
        get_rents = await self.model.objects.select_related("user").all()
        return get_rents

    async def create(self, schema: C2CCreate, user: models.User) -> C2C:
        obj_in_data = jsonable_encoder(schema)
        obj = C2C(**obj_in_data, user=user)

        return await super().create(obj)
    

c2c = CRUDUser(C2C)
