from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.language_models import ProgrammingLanguage
from schemas.language_schema import ProgrammingLanguageCreate

async def create_language(db: AsyncSession, language: ProgrammingLanguageCreate):
    new_lang = ProgrammingLanguage(
        name=language.name,
        description=language.description,
        image_url=language.image_url
    )
    db.add(new_lang)
    await db.commit()
    await db.refresh(new_lang)
    return new_lang

async def get_languages(db: AsyncSession):
    result = await db.execute(select(ProgrammingLanguage))
    return result.scalars().all()
