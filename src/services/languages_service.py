from sqlalchemy.orm import Session
from models.languages_model import ProgrammingLanguage
from schemas.languages_schema import ProgrammingLanguageCreate




def create_language(db: Session, language: ProgrammingLanguageCreate):
    new_lang = ProgrammingLanguage(
        name=language.name,
        description=language.description,
        # image_url=language.image_url
    )
    db.add(new_lang)
    db.commit()
    db.refresh(new_lang)
    return new_lang

def get_languages(db: Session):
    return db.query(ProgrammingLanguage).all()
