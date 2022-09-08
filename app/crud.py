from sqlalchemy.orm import Session

from . import models, schemas

def get_user_account(db: Session, user_account_id: int):
    return db.query(models.UserAccount).filter(models.UserAccount.id == user_account_id).first()

def get_event(db: Session, event_id: int):
    return db.query(models.Event).filter(models.Event.id == event_id).first()
    