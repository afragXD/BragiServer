
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, String, Integer, Column, Text, DateTime, Boolean, REAL, SMALLINT, Identity, select
from database.DTO import BookDTO
from database.DTO import ChapterDTO

from sqlalchemy import Connection

metadata = MetaData()
books = Table('books', metadata,
              Column('id', Integer(), Identity(start=1, increment=1, always=True, cycle=True), primary_key=True),
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

metadata2 = MetaData()
chapters = Table('chapters', metadata2,
              Column('id', Integer(),Identity(start=1, increment=1, always=True, cycle=True), primary_key=True),
              Column('chapter_number', Integer(), nullable=False),
              Column('chapter_name', Text(), nullable=False),
              Column('book_id', Integer()),

)

def getConnection()->Connection:
    engine = create_engine("postgresql+psycopg2://postgres:742617@localhost:5432/bragi")
    connection = engine.connect()
    return connection

def inseriFromParse(dto: BookDTO, connection: Connection):

    insert = books.insert().values(
        name = dto.name,
        en_name = dto.en_name,
        image = dto.image,
        description = dto.description,
        rating = dto.rating,
        status = dto.status,
        chapters = dto.chapters,
        year = dto.year,
        author = dto.author
    )
    connection.execute(insert)
    connection.commit()

def inseriChapter(dto: ChapterDTO, connection: Connection):

    insert = chapters.insert().values(
        chapter_number = dto.chapter_number,
        chapter_name = dto.chapter_name,
        book_id = dto.book_id
    )
    connection.execute(insert)
    connection.commit()

def getIdFromName(name: str, connection: Connection):
    id = select(books).where(
        books.c.en_name == name
    )
    id = connection.execute(id)

    return id.fetchone()[0]