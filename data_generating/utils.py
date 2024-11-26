from dataclasses import fields
from typing import Callable, Sequence

from pypika import Query, Table
from pypika.terms import ValueWrapper

from data_generating.factories.abstact import BaseModel
from data_generating.seeders import *


def generate_insert_query(instance: BaseModel, query: Query = None) -> str:
    # first_instance, model_type = instance, type(instances[0])
    # if any(type(instance) is not model_type for instance in instances):
    #     raise ValueError("All instances must be of the same type.")
    field_names = [f.name for f in fields(instance) if not f.name.startswith("_")]
    if not query:
        table = Table(instance.get_table_name())
        query = Query.into(table).columns(*[table[f_name] for f_name in field_names])

    query = query.insert(
        *[ValueWrapper(getattr(instance, f_name)) for f_name in field_names]
    )
    return query


def unique(gen: Callable[[], BaseModel], num_records) -> Sequence:
    unique_entities = set()
    while len(unique_entities) < num_records:
        unique_entities.add(gen())
    return list(set(unique_entities))
