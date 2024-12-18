from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import schemas
from controllers import post_controller

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostBase)
async def create_post(post: schemas.PostBase, db: Session = Depends(get_db)):
    return post_controller.create_post(post, db)

@router.delete('/{post_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int, db: Session = Depends(get_db)):
    post_controller.delete_post(post_id, db)

@router.get("/{post_id}", response_model=schemas.PostBase)
async def get_post(post_id: int, db: Session = Depends(get_db)):
    return post_controller.get_post(post_id, db)

@router.get("/", response_model=List[schemas.PostBase]) 
async def get_all(db: Session = Depends(get_db)):
    return post_controller.get_all(db)
