# models.py
from sqlalchemy import Column, Integer, String, DateTime
from database import Base
import datetime

class Log(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True)
    source = Column(String)
    ip = Column(String, nullable=True)
    event = Column(String)
    severity = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
