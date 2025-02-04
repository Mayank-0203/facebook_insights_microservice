from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Page(Base):
    __tablename__ = "pages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    url = Column(String, unique=True, index=True)
    profile_pic = Column(String)
    email = Column(String)
    website = Column(String)
    category = Column(String)
    followers = Column(Integer)
    likes = Column(Integer)
    creation_date = Column(DateTime)

    posts = relationship("Post", back_populates="page")

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    likes = Column(Integer)
    comments = Column(Integer)
    page_id = Column(Integer, ForeignKey("pages.id"))

    page = relationship("Page", back_populates="posts")
