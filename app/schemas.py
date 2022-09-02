from datetime import date, time
from typing import Union

from pydantic import BaseModel



class EventBase(BaseModel):
    name: str
    time: Union[time, None] = None
    date: Union[date, None] = None
    place: Union[str, None] = None



class EventCreate(EventBase):
    pass


class Event(EventBase):
    id: int
    
    class Config:
        orm_mode = True



class UserAccountBase(BaseModel):
    username: str
    email: str


class UserAccountCreate(UserAccountBase):
    password: str


class UserAccount(UserAccountBase):
    id: int

    class Config:
        orm_mode = True