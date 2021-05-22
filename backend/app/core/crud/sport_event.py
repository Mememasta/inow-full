from app.core.models.user import User
from fastapi.encoders import jsonable_encoder
from typing import Any, Dict, Optional, Union

from app.core.crud.base import CRUDBase
from app.core.models.sport_event import SportEvent
from app.core.schemas.sport_event import SportEventCreate, SportEventSchema, SportEventUpdate
from app.core import crud, models


class CRUDUser(CRUDBase[SportEvent, SportEventCreate, SportEventUpdate]):
    async def get(self, id: int) -> Optional[SportEvent]:
        get_event = await self.model.objects.select_related("organizer").select_related("members").get_or_none(pk=id)
        return get_event

    async def get_multy(self) -> Optional[SportEvent]:
        get_events = await self.model.objects.select_related("organizer").select_related("members").all()
        return get_events

    async def create(self, schema: Union[SportEventCreate, Dict[str, Any]], user: models.User) -> SportEvent:
        if isinstance(schema, dict):
            update_data = schema
        else:
            update_data = schema.dict(exclude_unset=True)
        update_data["organizer"] = user
        update_data["members"] = user
        print(update_data)

        return await super().create(update_data)

    async def to_participate(self, schema: SportEventSchema, user: models.User):
        pass

sport_event = CRUDUser(SportEvent)
