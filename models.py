from sqlalchemy import Boolean, Column, Integer, String, Date, DateTime, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Comment(Base):
    __tablename__ = 'comments'

    uid = Column(String(8), ForeignKey("users.id"), primary_key=True)
    tid = Column (Integer, ForeignKey("tasks.id"), primary_key=True)
    datetime = Column(DateTime, server_default=func.current_timestamp(), primary_key=True, nullable=False)
    contents = Column(String(255), nullable=False)

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    uid = Column(String(8), ForeignKey("users.id"), nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=False)

    comments = relationship("Comment", cascade="all, delete-orphan")

class User(Base):
    __tablename__ = 'users'

    id = Column(String(8), primary_key=True, index=True)
    name = Column(String(20), nullable=False)
    description = Column(String(255))
    date_created = Column(Date, server_default=func.current_date(), nullable=False)

    tasks = relationship("Task", cascade="all, delete-orphan")
    comments = relationship("Comment", cascade="all, delete-orphan")