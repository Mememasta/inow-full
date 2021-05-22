from typing import Any, Optional, List
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from app.core import crud, schemas, models
from app.api_v1 import deps


router = APIRouter()


@router.get("/{user_id}", response_model=Optional[schemas.C2CSchema])
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
    return await crud.c2c.create(schema=schema)

# @router.post("/open/create", response_model=schemas.UserSchema)
# async def create_user_open(
        # *,
        # email: EmailStr = Body(...),
        # password: str = Body(...)
# ) -> models.User:
    # user = await crud.user.get_by_email(email=email)
    # if user:
        # raise HTTPException(
            # status_code=400,
            # detail="The user with this email already exists in the system"
        # )
    # schema = schemas.UserCreate(password=password, email=email)
    # return await crud.user.create(schema=schema)

# @router.put("/update/{user_id}", response_model=Optional[schemas.UserSchema])
# async def update_user(
        # *,
        # user_id: int,
        # schema: schemas.UserUpdate,
        # current_user: models.User = Depends(deps.get_current_active_superuser)
# ) -> Optional[models.User]:
    # update_user = await crud.user.update(id=user_id, schema=schema)
    # if not update_user:
        # raise HTTPException(
            # status_code=404,
            # detail="The user with this id does not exists in the system"
        # )
    # return update_user

# @router.put("/update/me", response_model=Optional[schemas.UserSchema])
# async def update_user_me(
        # *, 
        # email: EmailStr = Body(None),
        # password: str = Body(None),
        # current_user: models.User = Depends(deps.get_current_active_user)
# ) -> Optional[models.User]:
    # current_user_data = jsonable_encoder(current_user)
    # schema = schemas.UserUpdate(**current_user_data)
    # if password is not None:
        # schema.password = password
    # else:
        # schema.password = ""
    # if email is not None:
        # schema.email = email
    # else:
        # schema.email = current_user.email
    # return await crud.user.update(id=current_user.id, schema=schema)

# @router.delete("/delete/{user_id}", response_model=Optional[models.User])
# async def delete_user(
        # *,
        # user_id: int,
        # current_user: models.User = Depends(deps.get_current_active_superuser)
# ) -> Any:
    # del_user = await crud.user.delete(id=user_id)
    # if not del_user:
        # raise HTTPException(
            # status_code=404,
            # detail="The user does not exist"
        # )
    # return del_user

# @router.delete("/delete/me", response_model=Optional[models.User])
# async def delete_user_me(
    # *,
    # email: EmailStr = Body(None),
    # password: str = Body(None),
    # current_user: models.User = Depends(deps.get_current_active_user)
# ) -> Optional[models.User]:
    # user = await crud.user.authenticate(email=email, password=password)
    # if user.id == current_user.id:
        # del_user = await crud.user.delete(id=current_user.id)
        # return del_user 
    # raise HTTPException(
        # status_code=404,
        # detail="Incorrect email or password"
    # )
