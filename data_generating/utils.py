from dataclasses import fields
from typing import Sequence

from pypika import Query, Table
from pypika.terms import ValueWrapper

from data_generating.factories.abstact import BaseModel
from data_generating.factories.models import Student


def generate_insert_query(instances: Sequence[BaseModel]) -> str:
    first_instance = instances[0]
    model_type = type(first_instance)
    if any(type(instance) is not model_type for instance in instances):
        raise ValueError("All instances must be of the same type.")

    table = Table(first_instance.get_table_name())
    field_names = [f.name for f in fields(first_instance) if not f.name.startswith("_")]

    query = Query.into(table).columns(*[table[f_name] for f_name in field_names])
    for instance in instances:
        query = query.insert(
            *[ValueWrapper(getattr(instance, f_name)) for f_name in field_names]
        )

    return str(query)


if __name__ == "__main__":
    students = [Student() for _ in range(5)]
    sql = generate_insert_query(students)
    print(sql)
