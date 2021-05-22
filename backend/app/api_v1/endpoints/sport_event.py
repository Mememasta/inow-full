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

@router.post("/create", response_model=schemas.SportEventSchema)
async def create_event(
    *,
    schema: schemas.SportEventCreate,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> models.SportEvent:
    event = await crud.sport_event.create(schema=schema, user=current_user)
    return event

@router.get("/to_participate/{event_id}", response_model=schemas.SportEventSchema)
async def to_participate(
        *,
        event_id: int,
        current_user: models.User = Depends(deps.get_current_active_user)
):
    return await crud.sport_event.to_participate(event_id=event_id, user=current_user)

@router.put("/update/{event_id}", response_model=schemas.SportEventSchema)
async def update_event(
    *,
    event_id: int,
    schema: schemas.SportEventUpdate,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Optional[models.SportEvent]:
    get_event = await crud.sport_event.get(id=event_id)
    if not get_event:
        raise HTTPException(status_code=404, detail="Event not found")
    if get_event.organizer.id == current_user.id:
        return await crud.sport_event.update(id=event_id, schema=schema)
    if not await crud.user.is_superuser(current_user):
        raise HTTPException(
                status_code=400,
                detail="The user doesn't have enough privileges"
        )
    return await crud.sport_event.update(id=event_id, schema=schema)

@router.delete("/delete/{event_id}", response_model=schemas.SportEventSchema)
async def delete_event(
    *,
    event_id: int,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Optional[models.SportEvent]:
    event = await crud.sport_event.get(id=event_id)
    if not event:
        raise HTTPException(
            status_code=404,
            detail="The event with this id does not exists in the system"
        )

    if event.organizer.id == current_user.id:
        del_event = await crud.sport_event.delete(id=event_id)
        return del_event
    if not await crud.user.is_superuser(current_user):
        raise HTTPException(
                status_code=400,
                detail="The user doesn't have enough privileges"
        )


