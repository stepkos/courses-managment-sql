from abc import ABC
from typing import Optional

from pydantic import BaseModel as _BaseModel
from pydantic import Field
from bson import ObjectId

from mongo_data_generating.models.utils import nullable_factory
from mongo_data_generating.models import fake


class BaseModel(_BaseModel, ABC):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class Answer(BaseModel):
    points: int | None = Field(
        default_factory=nullable_factory((lambda: fake.random_int(min=0, max=100)))
    )
    submitted_at: str = Field(default_factory=lambda: str(fake.date_time_this_year()))


class Question(BaseModel):
    content: str = Field(default_factory=fake.text)
    points: int = Field(default_factory=lambda: fake.random_int(min=0, max=100))


class File(BaseModel):
    file_url: str = Field(default_factory=fake.url)
    uploaded_at: str = Field(default_factory=lambda: str(fake.date_time_this_year()))
