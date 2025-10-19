from sqlalchemy import Column, Integer, String, Text
from database import Base 


class ProgrammingLanguage(Base):
    __tablename__ = "programming_languages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    image_url = Column(String(255), nullable=True)
