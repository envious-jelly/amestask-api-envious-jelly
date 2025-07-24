from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

'''
    uvicorn main:app --reload
'''

app = FastAPI()

models.Base.metadata.create_all(bind=engine) # ustvari mysql tabele če jih še ni

class UserBase(BaseModel):
    id: str
    name: str
    description: str

class TaskBase(BaseModel):
    uid: str
    title: str
    description: str

class CommentBase(BaseModel):
    uid: str
    tid: int
    contents: str


def get_db():
    db = SessionLocal()
    try:
        yield db # try to get
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/", status_code=status.HTTP_200_OK)
async def root(db: db_dependency):
    return None

@app.get("/users/", status_code=status.HTTP_200_OK)
async def read_all_users(db: db_dependency):
    return db.query(models.User).all()

@app.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def read_user(user_id: str, db: db_dependency):
    user = db.query(models.User).filter_by(id = user_id).first() # kot select ... where id == user_id
    if user is None:
        raise HTTPException(status_code=404, detail='Uporabnik ne obstaja')
    return user

@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    db_user = models.User(**user.model_dump()) # pretvori v model User
    db.add(db_user)
    db.commit()

@app.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: str, db: db_dependency):
    db_user = db.query(models.User).filter_by(id = user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail='Uporabnik ne obstaja')
    db.delete(db_user)
    db.commit()

@app.get("/tasks/", status_code=status.HTTP_200_OK)
async def read_all_tasks(db: db_dependency):
    return db.query(models.Task).all()

@app.post("/tasks/", status_code=status.HTTP_201_CREATED)
async def create_task(task: TaskBase, db: db_dependency):
    db_task = models.Task(**task.model_dump())
    db.add(db_task)
    db.commit()

@app.get("/comments/", status_code=status.HTTP_200_OK)
async def read_all_comments(db: db_dependency):
    return db.query(models.Comment).all()

@app.post("/comments/", status_code=status.HTTP_201_CREATED)
async def create_comment(comment: CommentBase, db: db_dependency):
    db_comment = models.Comment(**comment.model_dump())
    db.add(db_comment)
    db.commit()
