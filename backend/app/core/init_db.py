from app.core import crud, schemas
from app.core.config import settings


async def init_db() -> None:
    user = await crud.user.get_by_email(email=settings.FIRST_SUPERUSER_EMAIL)
    if not user:
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER_EMAIL,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            phone_number="89999999999",
            first_name="Morat",
            second_name="Chuchalov",
            is_superuser=True,
            is_active=True
        )
        user = await crud.user.create(schema=user_in)
