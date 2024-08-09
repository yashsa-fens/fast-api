from fastapi import APIRouter,Depends,status,HTTPException,Response
import repository.user
import schemas
import models
from typing import List
from database import *
from sqlalchemy.orm import Session
import hashing
import repository

router=APIRouter(
    prefix="/user",
    tags=['users']
)


@router.post("/",response_model=schemas.ShowUser)
def create_user(request:schemas.User,db:Session=Depends(get_db)):
    return repository.user.create(request,db)

@router.get("/{id}",response_model=schemas.ShowUser)
def get_user(id:int,db:Session=Depends(get_db)):
    return repository.user.show(id,db)

