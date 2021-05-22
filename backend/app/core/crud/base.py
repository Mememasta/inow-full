from typing import Generic, List, Optional, Type, TypeVar
from fastapi.encoders import jsonable_encoder
from ormar import Model
from pydantic.main import BaseModel


ModelType = TypeVar("ModelType", bound=Model)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]) -> None:
        self.model = model

    async def get(self, id: int) -> Optional[ModelType]:
        return await self.model.objects.get_or_none(pk=id)

    async def get_multy(self) -> List[Optional[ModelType]]:
        return await self.model.objects.all()

    async def create(self, schema: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(schema)
        return await self.model(**obj_in_data).save()

    async def update(self, id: int, schema: UpdateSchemaType) -> Optional[ModelType]:
        obj_in_data = jsonable_encoder(schema)
        obj = await self.get(id=id)
        if not obj:
            return None
        return await obj.update(**obj_in_data)

    async def delete(self, id: int) -> Optional[ModelType]:
        obj = await self.get(id=id)
        if not obj:
            return None
        await obj.delete()
        return obj
