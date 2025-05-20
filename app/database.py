# This file is crucial part of FastAPI + SQL Alchemy. It sets up the connection to PostgreSQL database
# and preps the environment for working with the database.

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

#loads environment variables from .env file into system's environment
load_dotenv()

#reads the "DATABASE_URL" from .env file; was enabled by loading them in previously
DATABASE_URL = os.getenv("DATABASE_URL")

#creates a database engine using connection URL; engine handles the actual communication with PostgreSQL server
engine = create_engine(DATABASE_URL)

# creates a session factory; sets the configs of creating a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# defines base, i.e the common superclass for all ORM models
Base = declarative_base() 

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()