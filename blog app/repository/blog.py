from fastapi import HTTPException,status
from sqlalchemy.orm import Session
import models
import schemas
def get_all(db:Session):
    blogs=db.query(models.Blog).all()
    return blogs

def create(request:schemas.Blog,db:Session):
    new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete(id,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id of {id} not found')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Done'

def update(id:int,request:schemas.Blog,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id of {id} not found')
    blog.update({'title':request.title,'body':request.body})
    db.commit()
    return 'updated'

def show(id:int,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        # response.status_code=status.HTTP_404_NOT_FOUND  
        # return {'Detail':f'blog with id {id} not found'}
        # this exception reduce line of code this below line done same work compare to above two line
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id {id} not found')
    return blog
