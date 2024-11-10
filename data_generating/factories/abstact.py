import random
import uuid
from abc import ABC
from dataclasses import dataclass, field

from data_generating.factories import fake
from data_generating.factories.utils import nullable_field

@dataclass(kw_only=True)
class BaseModel(ABC):
    _TABLE_NAME: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))


@dataclass(kw_only=True)
class User(BaseModel, ABC):
    first_name: str = field(default_factory=fake.first_name)
    surname: str = field(default_factory=fake.last_name)
    email: str = field(default_factory=fake.email)
    password: str = field(default_factory=lambda: fake.password(length=12))
    is_active: bool = field(
        default_factory=lambda: random.choices([True, False], weights=[75, 25])[0]
    )

@dataclass(kw_only=True)
class Answer(BaseModel):
    _TABLE_NAME: str = "answers"

    points: int | None = field(default_factory=nullable_field((lambda: fake.random_int(min=0, max=100))))
    submitted_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))

@dataclass(kw_only=True)
class Question(BaseModel):
    _TABLE_NAME: str = "questions"

    content: str = field(default_factory=fake.text)
    points: int = field(default_factory=lambda: fake.random_int(min=0, max=100))

@dataclass(kw_only=True)
class File(BaseModel):
    _TABLE_NAME: str = "files"

    file_url: str = field(default_factory=fake.url)
    uploaded_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))