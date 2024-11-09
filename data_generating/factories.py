import uuid
from abc import ABC
from dataclasses import dataclass, field
from faker import Faker
import random

fake = Faker("pl_PL")


@dataclass(kw_only=True)
class BaseFactory:
    id: str = field(default_factory=uuid.uuid4)


@dataclass(kw_only=True)
class UserFactory(BaseFactory):
    first_name: str = field(default_factory=fake.first_name)
    surname: str = field(default_factory=fake.last_name)
    email: str = field(default_factory=fake.email)
    password: str = field(default_factory=lambda: fake.password(length=12))
    is_active: bool = field(
        default_factory=lambda: random.choices([True, False], weights=[75, 25])[0]
    )


@dataclass(kw_only=True)
class StudentFactory(UserFactory):
    index: str = field(default_factory=lambda: fake.random_int(min=100000, max=999999))


@dataclass(kw_only=True)
class HostFactory(UserFactory):
    degree: str = field(default_factory=lambda: random.choices(["mgr", "dr", "prof"], weights=[75, 20, 5])[0])


@dataclass(kw_only=True)
class EntryFactory(BaseFactory):
    group_id: str
    host_id: str
    title: str = field(default_factory=fake.word)
    content: str = field(default_factory=fake.text)
    created_at: str = field(default_factory=fake.date_time_this_year)
    updated_at: str = field(default_factory=fake.date_time_this_year)


if __name__ == "__main__":
    student = StudentFactory()
    print(student)

    host = HostFactory()
    print(host)

    entry = EntryFactory(group_id="abcd", host_id=host.id)
    print(entry)
