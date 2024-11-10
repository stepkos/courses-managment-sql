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

    table = Table(first_instance._TABLE_NAME)
    query = Query.into(table).columns(
        *[
            table[f.name]
            for f in fields(first_instance)
            if not f.name.startswith('_')
        ]
    )

    for instance in instances:
        query = query.insert(
            *[
                ValueWrapper(getattr(instance, f.name))
                for f in fields(instance)
                if not f.name.startswith('_')
            ]
        )

    return str(query)


if __name__ == "__main__":
    students = [Student() for _ in range(5)]
    sql = generate_insert_query(students)
    print(sql)
