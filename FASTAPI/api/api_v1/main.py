from typing import List
from fastapi import Depends, HTTPException, Request,Response
from sqlalchemy.orm import Session
from core.db import curd, schemas
from fastapi import APIRouter

router = APIRouter()


# Dependency
def get_db(request: Request):
    return request.state.db


@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = curd.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return curd.create_user(db=db, user=user)


@router.get("/users/", response_model=List[schemas.User])
def read_users(response: Response, skip: int = 0, limit: int = 100, db: Session = Depends(get_db), ):
    users = curd.get_users(db, skip=skip, limit=limit)
    response.set_cookie('a','b')
    return users


@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = curd.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
        user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return curd.create_user_item(db=db, item=item, user_id=user_id)


@router.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = curd.get_items(db, skip=skip, limit=limit)
    return items
