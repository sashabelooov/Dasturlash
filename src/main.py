from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, declarative_base 
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:your_password@localhost:5432/you_db_name" 

engine = create_engine(SQLALCHEMY_DATABASE_URL) 

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

Base = declarative_base() 

async def get_db(): db = SessionLocal() try: yield db finally: db.close() 
async def create_table(): Base.metadata.create_all(bind=engine) 


from sqlalchemy import Column, Integer, String, Text 
from database import Base 


class ProgrammingLanguage(Base): 
    __tablename__ = "programming_languages" 
    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String(50), unique=True, nullable=False) 
    description = Column(Text, nullable=True) 
    logo_url = Column(String(255), nullable=True)