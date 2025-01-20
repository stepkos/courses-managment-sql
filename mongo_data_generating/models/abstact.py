from abc import ABC
from pydantic import BaseModel as _BaseModel
from pydantic import Field, EmailStr, HttpUrl, validator
from bson import ObjectId

from mongo_data_generating.models.utils import nullable_factory
from mongo_data_generating.models import fake


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class BaseModel(_BaseModel, ABC):
    _id: PyObjectId = Field(default_factory=ObjectId, alias="id")

    class Config:
        json_encoders = {ObjectId: str}


# class Answer(BaseModel):
#     points: int | None = Field(
#         default_factory=nullable_factory((lambda: fake.random_int(min=0, max=100)))
#     )
#     submitted_at: str = Field(default_factory=lambda: str(fake.date_time_this_year()))
#
#
# class Question(BaseModel):
#     content: str = Field(default_factory=fake.text)
#     points: int = Field(default_factory=lambda: fake.random_int(min=0, max=100))
#
#
# class File(BaseModel):
#     file_url: str = Field(default_factory=fake.url)
#     uploaded_at: str = Field(default_factory=lambda: str(fake.date_time_this_year()))
