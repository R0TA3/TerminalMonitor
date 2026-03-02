from dataclasses import dataclass
from datetime import datetime

@dataclass
class Event:
    timestamp: str
    source: str
    event_type: str
    src_ip: str = None
    dst_ip: str = None
    protocol: str = None
    message: str = None
    severity: str = "low"
