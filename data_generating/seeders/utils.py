from typing import Callable, Sequence
from factories.abstact import BaseModel


def unique(gen: Callable[[], BaseModel], num_records) -> Sequence:
    unique_entities = set()
    while len(unique_entities) < num_records:
        unique_entities.add(gen())
    return list(unique_entities)

