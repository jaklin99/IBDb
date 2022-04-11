from .config import settings
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DATETIME
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create a database URL for SQLAlchemy
SQLALCHEMY_DB_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
engine = create_engine(SQLALCHEMY_DB_URL) #what db I am using
SessionLocal = sessionmaker(autocommit=False, autoflush= False, bind = engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()