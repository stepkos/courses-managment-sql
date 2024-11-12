import random
import uuid
from abc import ABC
from dataclasses import dataclass, field

from data_generating.factories import fake
from data_generating.factories.utils import nullable_field


@dataclass(kw_only=True, frozen=True)
class BaseModel(ABC):
    _TABLE_NAME: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def get_table_name(self) -> str:
        return self._TABLE_NAME


@dataclass(kw_only=True, frozen=True)
class Answer(BaseModel):
    _TABLE_NAME: str = "answers"

    points: int | None = field(
        default_factory=nullable_field((lambda: fake.random_int(min=0, max=100)))
    )
    submitted_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))


@dataclass(kw_only=True, frozen=True)
class Question(BaseModel):
    _TABLE_NAME: str = "questions"

    content: str = field(default_factory=fake.text)
    points: int = field(default_factory=lambda: fake.random_int(min=0, max=100))


@dataclass(kw_only=True, frozen=True)
class File(BaseModel):
    _TABLE_NAME: str = "files"

    file_url: str = field(default_factory=fake.url)
    uploaded_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))
