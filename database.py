# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+psycopg2://splunkuser:yourpassword@localhost/splunkmini"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
import sqlite3

conn = sqlite3.connect("siem.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    source TEXT,
    event_type TEXT,
    src_ip TEXT,
    dst_ip TEXT,
    protocol TEXT,
    message TEXT,
    severity TEXT
)
""")

def log_event(event):
    c.execute("""
    INSERT INTO events VALUES (NULL,?,?,?,?,?,?,?,?)
    """, (
        event.timestamp, event.source, event.event_type,
        event.src_ip, event.dst_ip, event.protocol,
        event.message, event.severity
    ))
    conn.commit()
