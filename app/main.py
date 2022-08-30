from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import settings

SQLALCHEMY_DATABASE_URL = settings.db_url

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# import databases
# import ormar
# import sqlalchemy

# from datetime import date, time
# from fastapi import FastAPI
# from typing import Optional, List

# from .config import settings

# database = databases.Database(settings.db_url)
# metadata = sqlalchemy.MetaData()

# class BaseMeta(ormar.ModelMeta):
#     metadata = metadata
#     database = database


# class UserAccount(ormar.ModelMeta):
#     id: int = ormar.Integer(primary_key=True)
#     username: str = ormar.String(max_length=32, unique=True, nullable=False)
#     email: str = ormar.String(max_length=128, unique=True, nullable=False)
#     password: str = ormar.String(max_length=255, nullable=False)

#     class Meta(BaseMeta):
#         tablename = "user_account"


# class Event(ormar.ModelMeta):
#     id: int = ormar.Integer(primary_key=True)
#     name: str = ormar.String(max_length=128, nullable=False)
#     time: time = ormar.Time()
#     date: date = ormar.Date()
#     place: str = ormar.String(max_length=128)
#     users: Optional[List[UserAccount]] =  ormar.ManyToMany(UserAccount)

#     class Meta(BaseMeta):
#         tablename = "event"

# engine = sqlalchemy.create_engine(settings.db_url)
# metadata.create_all(engine)

# app = FastAPI()


# @app.get("/")
# async def index():
#     return {"app": "working!"}

# @app.on_event("startup")
# async def startup():
#     if not database.is_connected:
#         await database.connect()

# @app.on_event("shutdown")
# async def shutdown():
#     if database.is_connected:
#         await database.disconnect()
