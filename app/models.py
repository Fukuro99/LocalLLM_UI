from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel

class Note(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    done: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
