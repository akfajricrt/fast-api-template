from sqlalchemy.orm import Session
from fastapi import HTTPException
import models, schemas

def create_user(user: schemas.UserBase, db: Session):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(user_id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def get_all(db: Session):
    post = db.query(models.User).all()
    if not post:
        raise HTTPException(status_code=404, detail="User Data not found")
    return post
