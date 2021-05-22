from typing import Any, Optional, List
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from app.core import crud, schemas, models
from app.api_v1 import deps


router = APIRouter()
