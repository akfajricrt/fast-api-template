from sqlalchemy.orm import Session
from fastapi import HTTPException
import models, schemas

def create_post(post: schemas.PostBase, db: Session):
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_post(post_id: int, db: Session):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

def get_all(db: Session):
    post = db.query(models.Post).all()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

def delete_post(post_id: int, db: Session):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(post)
    db.commit()
    
