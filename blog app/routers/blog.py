from fastapi import APIRouter,Depends,status,HTTPException,Response
import repository.blog
import schemas
import models
from typing import List
from database import *
from sqlalchemy.orm import Session
import repository
from . import oauth2

router=APIRouter(
    tags=['blogs'],
    prefix="/blog"

)

@router.get("/",response_model=List[schemas.ShowBlog])
def get_all_blog(db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return repository.blog.get_all(db)

@router.post("/",status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return repository.blog.create(request,db)

@router.get("/{id}",response_model=schemas.ShowBlog)
def get_blog_by_id(id,response:Response,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
   return repository.blog.show(id,db)

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_blog_by_id(id,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return repository.blog.delete(id,db)

@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
def update_blog_by_id(request:schemas.Blog,id,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return repository.blog.update(id,request,db)
