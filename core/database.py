from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from decouple import config


USER = config("USER")
PASSWORD = config("PASSWORD")
HOST = config("HOST")
PORT = config("PORT")
DB_NAME = config("DB_NAME")

SQLALCHEMY_DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"


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