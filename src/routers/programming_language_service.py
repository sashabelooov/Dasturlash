from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.programming_language import ProgrammingLanguageCreate, ProgrammingLanguageRead
from services.programming_language_service import create_language, get_languages
from database import get_db


router = APIRouter(prefix="/languages", tags=["Programming Languages"])


@router.post("/", response_model=ProgrammingLanguageRead)
def add_language(language: ProgrammingLanguageCreate, db: Session = Depends(get_db)):
    return create_language(db, language)

@router.get("/", response_model=list[ProgrammingLanguageRead])
def list_languages(db: Session = Depends(get_db)):
    return get_languages(db)