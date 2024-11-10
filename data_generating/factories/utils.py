from typing import Callable, TypeVar
import random

T = TypeVar('T')

def nullable_field(
    generator: Callable[[], T], 
    probability_of_none: float = 0.5
) -> Callable[[], T | None]:
    return lambda: generator() if random.choice([True, False]) else None