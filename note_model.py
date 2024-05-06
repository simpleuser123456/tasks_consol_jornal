from datetime import datetime
from pydantic import BaseModel

class Note(BaseModel):
    id: int
    title: str
    body: str
    created_at: datetime = datetime.now()
    last_modified_at: datetime = datetime.now()

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }