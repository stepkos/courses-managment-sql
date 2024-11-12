import random
from typing import Callable, TypeVar, Sequence, Type, Iterable

T = TypeVar("T")


def nullable_field(
    generator: Callable[[], T], probability_of_none: float = 0.3
) -> Callable[[], T | None]:
    return lambda: generator() if random.random() < probability_of_none else None


def make_hashable(*fields: str) -> Type:
    class HashableMixin:
        def __hash__(self):
            return hash(tuple(getattr(self, field) for field in fields))

        def __eq__(self, other):
            if isinstance(other, self.__class__):
                return hash(self) == hash(other)
            return False

    return HashableMixin
