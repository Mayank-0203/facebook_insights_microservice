from pydantic import BaseModel
from datetime import datetime

class PageBase(BaseModel):
    name: str
    url: str
    profile_pic: str
    email: str
    website: str
    category: str
    followers: int
    likes: int
    creation_date: datetime

class PageCreate(PageBase):
    pass

class Page(PageBase):
    id: int

    class Config:
        orm_mode = True

class PostBase(BaseModel):
    content: str
    likes: int
    comments: int

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    page_id: int

    class Config:
        orm_mode = True
