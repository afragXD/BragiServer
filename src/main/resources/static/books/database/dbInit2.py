from sqlalchemy import create_engine, Identity
from sqlalchemy import MetaData, Table, String, Integer, Column, Text, DateTime, Boolean, REAL, SMALLINT, ForeignKey

engine = create_engine("postgresql+psycopg2://postgres:742617@localhost:5432/bragi")
#connection = engine.connect()

metadata = MetaData()
chapters = Table('chapters', metadata,
              Column('id', Integer(),Identity(start=1, increment=1, always=True, cycle=True), primary_key=True),
              Column('chapter_number', Integer(), nullable=False),
              Column('chapter_name', Text(), nullable=False),
              Column('book_id', Integer()),

)

metadata.create_all(engine)