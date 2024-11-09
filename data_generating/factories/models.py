import random
from dataclasses import dataclass, field

from data_generating.factories import fake
from data_generating.factories.abstact import BaseFactory, UserFactory


@dataclass(kw_only=True)
class StudentFactory(UserFactory):
    index: str = field(default_factory=lambda: fake.random_int(min=100000, max=999999))


@dataclass(kw_only=True)
class HostFactory(UserFactory):
    degree: str = field(
        default_factory=lambda: random.choices(
            ["mgr", "dr", "prof"], weights=[75, 20, 5]
        )[0]
    )


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
