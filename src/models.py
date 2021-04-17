import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("user.user_id"))
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("user.user_id"))
    user_from_id = Column(String(250))
    user_to_id = Column(String(250))
    
    def to_dict(self):
        return {}

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("user.user_id"))
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer)
    post_id = Column(Integer)

    def to_dict(self):
        return {}

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("user.user_id"))

    def to_dict(self):
        return {}   

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("user.user_id"))
    type = Column(String(250))
    url = Column(String(250))
    post_id = Column(Integer)

    def to_dict(self):
        return {}  

render_er(Base, 'diagram.png')