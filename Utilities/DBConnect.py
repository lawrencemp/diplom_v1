import sqlite3
import Models
from sqlalchemy import create_engine
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase

sqlite_database: str = "sqlite:///find_laptop.db"
engine = create_engine(sqlite_database)


class Base(DeclarativeBase):
    pass

class TopLaptop(Base):
    __tablename__ = "top_laptop"
    id = Column(Integer, primary_key=True, index=True)
    price_segment_id = Column(Integer, ForeignKey("price_segments.id"))
    link = Column(String)


class PriceSegment(Base):
    __tablename__ = "price_segments"
    id = Column(Integer, primary_key=True, index=True)
    bottom_line = Column(Integer)
    top_line = Column(Integer)



