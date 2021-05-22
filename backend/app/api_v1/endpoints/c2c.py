from typing import Any, Optional, List
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from app.core import crud, schemas, models
from app.api_v1 import deps


router = APIRouter()


@router.get("/{rent_id}", response_model=Optional[schemas.C2CSchema])
async def get_rent_by_id(
        *,
        rent_id: int,
        current_user: models.User = Depends(deps.get_current_active_user)
) -> Optional[models.C2C]:
    rent_by_id = await crud.c2c.get(id=rent_id)
    if not rent_by_id:
        raise HTTPException(
            status_code=404,
            detail="Not found"
        )
    return rent_by_id

# @router.get("/me", response_model=Optional[schemas.UserSchema])
# async def get_user_me(
    # current_user: models.User = Depends(deps.get_current_active_user)
# ) -> Optional[models.User]:
    # return current_user

@router.get("/", response_model=List[schemas.C2CSchema])
async def get_rents(
        current_user: models.User = Depends(deps.get_current_active_user)
) -> List[Optional[models.C2C]]:
    return await crud.c2c.get_multy()

@router.post("/create", response_model=schemas.C2CSchema)
async def create_rent(
        *,
        schema: schemas.C2CCreate,
        current_user: models.User = Depends(deps.get_current_active_user)
) -> models.C2C:
    return await crud.c2c.create(schema=schema, user=current_user)

@router.put("/update/{rent_id}", response_model=Optional[schemas.C2CSchema])
async def update_user(
        *,
        rent_id: int,
        schema: schemas.C2CUpdate,
        current_user: models.User = Depends(deps.get_current_active_user)
) -> Optional[models.C2C]:
    rent = await crud.c2c.get(id=rent_id)
    if not rent:
        raise HTTPException(
            status_code=404,
            detail="The rent with this id does not exists in the system"
        )

    if rent.user.id == current_user.id:
        update_rent = await crud.c2c.update(id=rent_id, schema=schema)
        return update_rent

    if not await crud.user.is_superuser(current_user):
        raise HTTPException(
                status_code=400,
                detail="The rent doesn't have enough privileges"
        )

@router.delete("/delete/{rent_id}", response_model=Optional[schemas.C2CSchema])
async def delete_user(
        *,
        rent_id: int,
        current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    rent = await crud.c2c.get(id=rent_id)
    if not rent:
        raise HTTPException(
            status_code=404,
            detail="The rent with this id does not exists in the system"
        )

    if rent.user.id == current_user.id:
        del_rent = await crud.c2c.delete(id=rent_id)
        return del_rent
    if not await crud.user.is_superuser(current_user):
        raise HTTPException(
                status_code=400,
                detail="The rent doesn't have enough privileges"
        )
