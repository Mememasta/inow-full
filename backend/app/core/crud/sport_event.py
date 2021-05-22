from fastapi.encoders import jsonable_encoder
from typing import Any, Dict, Optional, Union

from app.core.crud.base import CRUDBase
from app.core.models.sport_event import SportEvent
from app.core.schemas.sport_event import SportEventCreate, SportEventUpdate
from app.core import crud, models


class CRUDUser(CRUDBase[SportEvent, SportEventCreate, SportEventUpdate]):
    async def get(self, id: int) -> Optional[SportEvent]:
        get_event = await self.model.objects.select_related("user").get_or_none(pk=id)
        return get_event

    async def get_multy(self) -> Optional[SportEvent]:
        get_events = await self.model.objects.select_related("user").all()
        return get_events

    async def create(self, schema: Union[SportEventCreate, Dict[str, Any]], user: models.User) -> SportEvent:
        if isinstance(schema, dict):
            update_data = schema
        else:
            update_data = schema.dict(exclude_unset=True)
        update_data["user"] = user
        print(update_data)

        return await super().create(update_data)

sport_event = CRUDUser(SportEvent)
