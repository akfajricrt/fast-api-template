from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import schemas
from controllers import user_controller

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserBase)
async def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    return user_controller.create_user(user, db)

@router.get("/{user_id}", response_model=schemas.UserBase)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    return user_controller.get_user(user_id, db)

@router.get("/", response_model=List[schemas.UserBase])
async def get_all(db: Session = Depends(get_db)):
    return user_controller.get_all(db)
