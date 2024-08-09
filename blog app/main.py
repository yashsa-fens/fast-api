from fastapi import FastAPI,Depends,status,Response,HTTPException
from sqlalchemy.orm import Session
from typing import List
import schemas
import models
import hashing
from routers import blog,user,authentication

app =FastAPI()
from database import *

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)
# @app.get("/blog")   
# def index(limit=10,published:bool=True,sort:str|None=None):
#     if published:
#        return {'data':f'{limit} published blogs from db'}
#     else:
#        return {'data' : f'{limit} unpublished blogs from db'}
       

# @app.get("/about")
# def index2():
#     return {'data':'about page'}

# @app.get("/blog/unpublished")
# def unplublished():
#     return {'data':'all unpublished blog'}

# @app.get("/blog/{id}")
# def getId(id:int):
#     return {'data':id}

# when server run creating all model in database
models.Base.metadata.create_all(bind=engine)

