from typing import Callable, Sequence
from data_generating.factories import BaseModel

def unique(gen: Callable[[], BaseModel], num_records) -> Sequence[BaseModel]:
    unique_entities = set()
    while len(unique_entities) < num_records:
        unique_entities.add(gen())
    return Sequence(unique_entities)

