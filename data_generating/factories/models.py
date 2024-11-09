import random
from dataclasses import dataclass, field

from data_generating.factories import fake
from data_generating.factories.abstact import BaseModel, User


@dataclass(kw_only=True)
class Student(User):
    _TABLE_NAME: str = "students"

    index: str = field(default_factory=lambda: fake.random_int(min=100000, max=999999))


@dataclass(kw_only=True)
class Host(User):
    _TABLE_NAME: str = "hosts"

    degree: str = field(
        default_factory=lambda: random.choices(
            ["mgr", "dr", "prof"], weights=[75, 20, 5]
        )[0]
    )


@dataclass(kw_only=True)
class Entry(BaseModel):
    _TABLE_NAME: str = "entries"

    group_id: str
    host_id: str
    title: str = field(default_factory=fake.word)
    content: str = field(default_factory=fake.text)
    created_at: str = field(default_factory=fake.date_time_this_year)
    updated_at: str = field(default_factory=fake.date_time_this_year)


if __name__ == "__main__":
    student = Student()
    print(student)

    host = Host()
    print(host)

    entry = Entry(group_id="abcd", host_id=host.id)
    print(entry)
