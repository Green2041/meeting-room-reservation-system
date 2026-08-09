import os
from typing import Annotated
from fastapi import Depends
from sqlmodel import Field, Session, SQLModel, create_engine, select
from dotenv import load_dotenv


# Step 2 — Postgres connection + session dependency

# Part A: Load connection string from .env & create engine
# Load the db from the .env connection string
load_dotenv()           # dotenv locates the .env file
db_url = os.environ.get("DATABASE_URL")        # Pull the database connection string from the .env

# Create the engine
engine = create_engine(db_url)

# Part B: Create a Session Dependency
def get_session():                          # Opens a new session (i.e. temp workspace for postgres)
    with Session(engine) as session:
        yield session                       # yield hands session object back to endpoint for use
    # <-- get_session() will tear down the session after returned to yield

SessionDep = Annotated[Session, Depends(get_session)]   # Reusable alias to call get_session()


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)