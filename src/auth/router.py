from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import service, schemas
from ..database import get_db

router = APIRouter()

@router.post('/sign-up')
async def sign_up(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return service.create_user(user=user, db=db)