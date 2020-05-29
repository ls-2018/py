from typing import List
from fastapi import Depends, HTTPException, Response
from core.peewee_db import curd, schemas
from fastapi import APIRouter
from core.peewee_db.database import get_db

router = APIRouter()


@router.get("/users/", response_model=List[schemas.User], dependencies=[Depends(get_db)])
def read_users(response: Response, skip: int = 0, limit: int = 100):
    users = curd.get_users(skip=skip, limit=limit)
    response.set_cookie('a', 'b')
    response.headers["X-Cat-Dog"] = "alone in the world"
    response.status_code = 200
    return users


@router.get("/users/{user_id}", response_model=schemas.User, dependencies=[Depends(get_db)])
def read_user(user_id: int, ):
    db_user = curd.get_user(user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
