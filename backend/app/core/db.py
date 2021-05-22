import sqlalchemy
import databases


from app.core.config import settings


database = databases.Database(str(settings.SQLALCHEMY_DATABASE_URI))
metadata = sqlalchemy.MetaData()

from app.core import schemas, models

engine = sqlalchemy.create_engine(str(settings.SQLALCHEMY_DATABASE_URI))
metadata.drop_all(engine)
metadata.create_all(engine)
