from dataclasses import dataclass
from typing import Optional, List


@dataclass
class MessageSMS:
    message: str
    sender: str
    to: str


@dataclass
class MessageEmail:
    subject: str
    message: str
    sender: str
    to: str
    cc: Optional[List[str]]
    cco: Optional[List[str]]