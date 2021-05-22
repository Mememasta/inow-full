from datetime import timedelta

from typing import Any
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pydantic.networks import EmailStr

from app.core import models, schemas, crud
from app.core.config import settings
from app.core import security
from app.api_v1 import deps

from app.core.utils import (
        generate_password_reset_token,
        verify_password_reset_token,
        send_reset_password_email,
)


router = APIRouter()

@router.post("/login/access-token", response_model=schemas.Token)
async def login_access_token(
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    user = await crud.user.authenticate(email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="Incorrect email or password"
        )
    elif not await crud.user.is_active(user=user):
        raise HTTPException(
                status_code=400,
                detail="Inactive user"
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": await security.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }

@router.post("/test-token", response_model=models.User)
async def test_token(
    current_user: models.User = Depends(deps.get_current_user)
) -> models.User:
    return current_user

@router.post("/password-recovery/{email}", response_model=schemas.Msg)
async def recovery_password(
    email: EmailStr
) -> Any:
    user = await crud.user.get_by_email(email=email)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this email does not exist in the system"
        )
    password_reset_token = await generate_password_reset_token(email=email)
    await send_reset_password_email(
        email_to=user.email, email=email, token=password_reset_token
    )
    return {"msg": "Password recovery email sent"}

