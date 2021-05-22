from fastapi.encoders import jsonable_encoder
from typing import Any, Dict, Optional, Union

from app.core.crud.base import CRUDBase
from app.core.models.sport_event import SportEvent
from app.core.schemas.sport_event import SportEventCreate, SportEventUpdate


class CRUDUser(CRUDBase[SportEvent, SportEventCreate, SportEventUpdate]):
    pass

sport_event = CRUDUser(SportEvent)
