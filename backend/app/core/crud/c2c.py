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

    async def create(self, schema: Union[C2CCreate, Dict[str, Any]], user: models.User) -> C2C:
        if isinstance(schema, dict):
            update_data = schema
        else:
            update_data = schema.dict(exclude_unset=True)
        update_data["user"] = user
        print(update_data)

        return await super().create(update_data)
    

c2c = CRUDUser(C2C)
