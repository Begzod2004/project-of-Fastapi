from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABES_URL = 'sqlite:///./cotegory.db'

engine = create_engine(SQLALCHEMY_DATABES_URL, connect_args=({"check_same_thread": False}))

SessionLokal = sessionmaker(bind=engine, autocommit=False, autoflush=False,)

Base = declarative_base()