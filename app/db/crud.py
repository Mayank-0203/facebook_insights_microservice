from sqlalchemy.orm import Session
from app.db import models, schemas

# Page CRUD operations
def get_page(db: Session, page_id: int):
    return db.query(models.Page).filter(models.Page.id == page_id).first()

def get_page_by_url(db: Session, url: str):
    return db.query(models.Page).filter(models.Page.url == url).first()

def get_pages(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Page).offset(skip).limit(limit).all()

def create_page(db: Session, page: schemas.PageCreate):
    db_page = models.Page(**page.dict())
    db.add(db_page)
    db.commit()
    db.refresh(db_page)
    return db_page

# Post CRUD operations
def get_posts(db: Session, page_id: int):
    return db.query(models.Post).filter(models.Post.page_id == page_id).all()

def create_post(db: Session, post: schemas.PostCreate, page_id: int):
    db_post = models.Post(**post.dict(), page_id=page_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
