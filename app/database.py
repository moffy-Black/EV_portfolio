from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from env import DB_USER,DB_PASSWORD,DB_HOST,DB_NAME

DATABASE = f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}?charset=utf8"

engine = create_engine(
    DATABASE,
    encoding='utf-8',
    echo=True
)

SessionLocal = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflus=False,
        bind=engine
    )
)

Base = declarative_base()
Base.query = SessionLocal.query_property()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()