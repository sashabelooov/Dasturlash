from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.language_schema import ProgrammingLanguageCreate, ProgrammingLanguageRead
from services.languages_service import create_language, get_languages
from core.database import get_db

router = APIRouter(prefix="/languages", tags=["Programming Languages"])

@router.post("/", response_model=ProgrammingLanguageRead)
async def add_language(language: ProgrammingLanguageCreate, db: AsyncSession = Depends(get_db)):
    return await create_language(db, language)

@router.get("/", response_model=list[ProgrammingLanguageRead])
async def list_languages(db: AsyncSession = Depends(get_db)):
    return await get_languages(db)
