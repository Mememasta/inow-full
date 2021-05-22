from fastapi import APIRouter
from app.api_v1.endpoints import login, user, c2c, sport_event


api_router = APIRouter()

api_router.include_router(login.router, prefix="", tags=['login'])
api_router.include_router(user.router, prefix="/user", tags=['user'])
api_router.include_router(c2c.router, prefix="/rent", tags=['c2c_rent'])
api_router.include_router(sport_event.router, prefix="/event", tags=['event'])
