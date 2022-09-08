from sqlalchemy import Column, ForeignKey, Integer, String, Table, Time, Date
from sqlalchemy.orm import relationship, Session

from .database import Base, engine


user_event = Table(
    "association",
    Base.metadata,
    Column("user_id", ForeignKey("user_account.id"), primary_key=True),
    Column("event_id", ForeignKey("event.id"), primary_key=True),
)


class UserAccount(Base):
    __tablename__ = "user_account"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(128), unique=True, nullable=False)
    password = Column(String(256), nullable=False)
    username = Column(String(32), unique=True, nullable=False)

    events = relationship("Event", secondary=user_event, back_populates="users")


class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    time = Column(Time)
    date = Column(Date)
    place = Column(String(128))

    users = relationship("UserAccount", secondary=user_event, back_populates="events")
