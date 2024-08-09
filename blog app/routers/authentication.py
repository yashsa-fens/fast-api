from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
import schemas
import database
import models
import hashing
import token_1
from datetime import datetime,timedelta
from fastapi.security import OAuth2PasswordRequestForm
router=APIRouter( 
    tags=['authentication']
)


@router.post("/login")
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Invalid Credentials')
    if not hashing.Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Invalid Password')
    access_token = token_1.create_access_token(data={"sub": user.email})
    return {'access_token':access_token, 'token_type':"bearer"}

