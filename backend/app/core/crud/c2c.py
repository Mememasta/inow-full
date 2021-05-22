from fastapi.encoders import jsonable_encoder
from typing import Any, Dict, Optional, Union

from app.core.crud.base import CRUDBase
from app.core.models.c2c import C2C
from app.core.schemas.c2c import C2CCreate, C2CUpdate


class CRUDUser(CRUDBase[C2C, C2CCreate, C2CUpdate]):
    async def get(self, id: int) -> Optional[C2C]:
        get_rent = await self.model.objects.select_related("users").get_or_none(pk=id)
        return get_rent

    async def create(self, schema: C2CCreate) -> C2C:
        get_expert = await Expert.objects.get_or_none(pk=schema.expert_id)
        get_customer = await Customer.objects.get_or_none(pk=schema.customer_id)
        if not(get_customer and get_expert):
            return None
        return await super().create(schema)

c2c = CRUDUser(C2C)
