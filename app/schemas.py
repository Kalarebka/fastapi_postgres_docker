from datetime import date, time
from typing import ForwardRef, List, Union

from pydantic import BaseModel

# Takes care of the classes referencing each other
UserAccount = ForwardRef("UserAccount")

class EventBase(BaseModel):
    name: str
    time: Union[time, None]
    date: Union[date, None]
    place: Union[str, None]


class EventCreate(EventBase):
    pass


class Event(EventBase):
    id: int
    users: List[UserAccount] = []

    class Config:
        orm_mode = True


class UserAccountBase(BaseModel):
    username: str
    email: str


class UserAccountCreate(UserAccountBase):
    password: str


class UserAccount(UserAccountBase):
    id: int
    events: List[Event] = []

    class Config:
        orm_mode = True

# Takes care of the classes referencing each other
Event.update_forward_refs()
