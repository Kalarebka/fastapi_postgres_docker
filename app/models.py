from datetime import time, date
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, Session

from .database import Base, engine


UserEvent = Table("UserEvent",
                Column("id", Integer, primary_key=True),
                Column("user_id", Integer, ForeignKey("UserAccount.id")),
                Column("event_id", Integer, ForeignKey("Event.id")))
                

class UserAccount(Base):
    __tablename__ = "user_account"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, max_length=128)
    hashed_password = Column(String, max_length=256)
    username = Column(String, unique=True, max_length=32)

    events = relationship("Event", secondary=UserEvent, backref="UserAccount")


class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, max_length=128, nullable=False)
    time = Column(time)
    date = Column(date)
    place = Column(String, max_length=128)


    users = relationship("UserAccount", secondary=UserEvent, backref="Event")




Base.metadata.create_all(engine)