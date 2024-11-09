import random
import uuid
from abc import ABC
from dataclasses import dataclass, field

from data_generating.factories import fake


@dataclass(kw_only=True)
class BaseFactory(ABC):
    id: str = field(default_factory=uuid.uuid4)


@dataclass(kw_only=True)
class UserFactory(BaseFactory, ABC):
    first_name: str = field(default_factory=fake.first_name)
    surname: str = field(default_factory=fake.last_name)
    email: str = field(default_factory=fake.email)
    password: str = field(default_factory=lambda: fake.password(length=12))
    is_active: bool = field(
        default_factory=lambda: random.choices([True, False], weights=[75, 25])[0]
    )
