from sqlalchemy import create_engine, Identity
from sqlalchemy import MetaData, Table, String, Integer, Column, Text, DateTime, Boolean, REAL, SMALLINT

engine = create_engine("postgresql+psycopg2://postgres:742617@localhost:5432/bragi")
#connection = engine.connect()

metadata = MetaData()
books = Table('books', metadata,
              Column('id', Integer(),Identity(start=1, increment=1, always=True, cycle=True), primary_key=True),
              Column('name', Text(), nullable=False),
              Column('en_name', Text(), nullable=False),
              Column('image', Text(), nullable=False),
              Column('description', Text(), nullable=False),
              Column('rating', REAL(), nullable=False),
              Column('status', String(15), nullable=False, default='Завершено'),
              Column('chapters', SMALLINT(), nullable=False),
              Column('year', SMALLINT(), nullable=False),
              Column('author', Text(), nullable=False),
)

metadata.create_all(engine)