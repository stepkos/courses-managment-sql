import random
from typing import Callable, TypeVar, Sequence

T = TypeVar("T")


def nullable_field(
    generator: Callable[[], T], probability_of_none: float = 0.5
) -> Callable[[], T | None]:
    return lambda: generator() if random.choice([True, False]) else None


def make_hashable(field_names: Sequence[str] | str):
    class HashableMixin:
        def __hash__(self):
            if isinstance(field_names, str):
                return hash(getattr(self, field_names))
            return hash(tuple(getattr(self, field_name) for field_name in field_names))

        def __eq__(self, other):
            if isinstance(other, self.__class__):
                return hash(self) == hash(other)
            return False

    return HashableMixin
