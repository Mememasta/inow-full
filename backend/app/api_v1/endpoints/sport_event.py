from typing import Any, Optional, List
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from app.core import crud, schemas, models
from app.api_v1 import deps


router = APIRouter()

@router.get("/{event_id}", response_model=Optional[schemas.SportEventSchema])
async def get_event(
    *,
    event_id: int,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> models.SportEvent:
    event = await crud.sport_event.get(id=event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.get("/", response_model=List[Optional[schemas.SportEventSchema]])
async def get_events(
    current_user: models.User = Depends(deps.get_current_active_user)
) -> List[Optional[models.SportEvent]]:
    events = await crud.sport_event.get_multy()
    return events

@router.post("/create", response_model=schemas.SportEventCreate)
async def create_event(
    *,
    schema: schemas.SportEventCreate,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> models.SportEvent:
    event = await crud.sport_event.create(schema=schema, user=current_user)
    return event

@router.put("/update/{event_id}", response_model=schemas.SportEventUpdate)
async def update_event(
    *,
    event_id: int,
    schema: schemas.SportEventUpdate,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> models.SportEvent:
    get_event = await crud.sport_event.get(id=event_id)
    if not get_event:
        raise HTTPException(status_code=404, detail="Event not found")
    if not event:
        return {}

