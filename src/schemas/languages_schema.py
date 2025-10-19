from pydantic import BaseModel

class ProgrammingLanguageBase(BaseModel):
    name: str
    description: str | None = None
    image_url: str | None = None

class ProgrammingLanguageCreate(ProgrammingLanguageBase):
    pass

class ProgrammingLanguageRead(ProgrammingLanguageBase):
    id: int

    class Config:
        orm_mode = True
