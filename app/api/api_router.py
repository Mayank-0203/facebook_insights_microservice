from fastapi import APIRouter
from app.api.endpoints import page

api_router = APIRouter()
api_router.include_router(page.router, prefix="/pages", tags=["pages"])
