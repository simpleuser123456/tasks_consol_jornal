from datetime import datetime
from pydantic import BaseModel

class Note(BaseModel):
    id: int
    title: str
    body: str
    last_modified_at: datetime = datetime.now()

    @classmethod
    def __get_validators__(cls):
        yield cls.model_validate

    @classmethod
    def validate(cls, v: datetime):
        return v.isoformat()

    def dict(self, **kwargs):
        data = super().dict(**kwargs)
        data['last_modified_at'] = self.last_modified_at.isoformat()
        return data