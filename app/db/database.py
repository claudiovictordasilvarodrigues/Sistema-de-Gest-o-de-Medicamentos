from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarite_base

DATABASE = "sqlite:///./test.db"

engine = create_engine(
    DATABASE, 
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bing = engine
)

Base = declarite_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()