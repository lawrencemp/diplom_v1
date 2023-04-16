from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

sqlite_database: str = "sqlite:///DatabaseUtilities/find_laptop.db"
engine = create_engine(sqlite_database)
Session = sessionmaker(autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


class TopLaptop(Base):
    __tablename__ = "top_laptop"
    id = Column(Integer, primary_key=True, index=True)
    price_segment_id = Column(Integer, ForeignKey("price_segments.id"))
    score = Column(Integer)
    link = Column(String)


class PriceSegment(Base):
    __tablename__ = "price_segments"
    id = Column(Integer, primary_key=True, index=True)
    bottom_line = Column(Integer)
    top_line = Column(Integer)


class CpuBenchData(Base):
    __tablename__ = "cpu"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cpu_name = Column(String)
    geekbench_multiprocess = Column(Integer)


class GpuBenchData(Base):
    __tablename__ = "gpu"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    gpu_name = Column(String)
    bench_score = Column(Integer)







