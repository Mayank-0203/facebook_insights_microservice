from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import models, schemas, crud
from app.core.dependencies import get_db
from app.services.scraper import scrape_facebook_page

router = APIRouter()

@router.post("/", response_model=schemas.Page)
def create_page(page: schemas.PageCreate, db: Session = Depends(get_db)):
    return crud.create_page(db, page=page)

@router.get("/{username}/scrape", response_model=schemas.Page)
def scrape_and_create_page(username: str, db: Session = Depends(get_db)):
    # Check if page exists in DB
    db_page = db.query(models.Page).filter(models.Page.url == f"https://www.example.com/{username}").first()
    if db_page:
        return db_page
    
    # Scrape the page if not in DB
    page_data = scrape_facebook_page(username)
    page_in = schemas.PageCreate(**page_data)
    return crud.create_page(db, page=page_in)

@router.get("/{page_id}", response_model=schemas.Page)
def read_page(page_id: int, db: Session = Depends(get_db)):
    db_page = crud.get_page(db, page_id=page_id)
    if db_page is None:
        raise HTTPException(status_code=404, detail="Page not found")
    return db_page

@router.get("/", response_model=list[schemas.Page])
def read_pages(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    pages = crud.get_pages(db, skip=skip, limit=limit)
    return pages
