from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'postgresql://usuario_prueba:PWD123@172.30.1.10:5432/demo_db'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class TimeZoneData(Base):
    __tablename__ = 'country_time_zones'

    id = Column(Integer, primary_key=True)
    country_code = Column(Text)
    country_name = Column(Text)
    time_zone = Column(Text)
    gmt_offset = Column(Text)