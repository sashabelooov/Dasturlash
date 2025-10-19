from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:2323@localhost:5432/postgres"


engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def create_table():
    Base.metadata.create_all(bind=engine)