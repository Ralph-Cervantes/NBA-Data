import os
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base


PG_PASSWORD = 'PG_PASSWORD'
PG_USERNAME = 'PG_USERNAME'
PG_DB_NAME  = 'PG_DB'

password    = os.getenv(PG_PASSWORD)
username    = os.getenv(PG_USERNAME)
db_name     = os.getenv(PG_DB_NAME)

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    
    url = Column(Integer, primary_key=True)
    title = Column(String)
    product_type = Column(String)
    price_excl_tax = Column(Float)
    price_incl_tax = Column(Float)
    tax = Column(Float)
    num_reviews = Column(Integer)
    stars = Column(Integer)
    category = Column(String)
    price = Column(Float)
    
    
db_url = f'postgresql+psycopg2://{username}:{password}@localhost:5432/{db_name}'
engine = create_engine(db_url)
Base.metadata.create_all(engine)