import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

username = os.environ['POSTGRES_USER']
passwd = os.environ['POSTGRES_PASSWORD']

engine = create_engine('postgresql://'+username+':'+passwd+'@stancu.co:5432/'+username)

db_session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
    ))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # Import modules here so you don't have to import them everywhere you use them
    import models
    Base.metadata.create_all(bind=engine)
