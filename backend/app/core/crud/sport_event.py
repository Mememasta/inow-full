from app.core.models.user import User
from fastapi.encoders import jsonable_encoder
from typing import Any, Dict, Optional, Union

from app.core.crud.base import CRUDBase
from app.core.models.sport_event import SportEvent
from app.core.schemas.sport_event import SportEventCreate, SportEventSchema, SportEventUpdate
from app.core import crud, models


class CRUDUser(CRUDBase[SportEvent, SportEventCreate, SportEventUpdate]):
    async def get(self, id: int) -> Optional[SportEvent]:
        get_event = await self.model.objects.select_related(["organizer", "members"]).get_or_none(pk=id)
        return get_event

    async def get_multy(self) -> Optional[SportEvent]:
        get_events = await self.model.objects.select_related(["members", "organizer"]).all()
        return get_events

    async def create(self, schema: SportEventCreate, user: models.User) -> SportEvent:
        obj_in_data = jsonable_encoder(schema)
        obj = SportEvent(**obj_in_data, organizer=user)
        event = await super().create(obj)
        obj_in_db = await event.members.add(user)
        return event

    async def to_participate(self, event_id: int, user: models.User) -> Any:
        get_event = await self.get(id=event_id)
        await get_event.members.add(user)
        return get_event
        
        

sport_event = CRUDUser(SportEvent)
