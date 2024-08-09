from fastapi import HTTPException,status
from sqlalchemy.orm import Session
import models
import schemas
import hashing

def create(request:schemas.User,db:Session):
    new_user=models.User(name=request.name,email=request.email,password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id:int,db:Session):
    user=db.query(models.User).filter(id==models.User.id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'user with id {id} not found.')
    return user