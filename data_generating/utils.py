from typing import Sequence

from pypika import Query, Table
from pypika.terms import ValueWrapper

from data_generating.factories.abstact import BaseModel
from data_generating.factories.models import Student


def generate_insert_query(instances: Sequence[BaseModel]) -> str:
    first_instance = instances[0]
    table = Table(first_instance._TABLE_NAME)
    query = Query.into(table).columns(
        *[table[f.name] for f in first_instance.__dataclass_fields__.values()]
    )

    for instance in instances:
        if type(instance) is not type(first_instance):
            raise ValueError("All instances must be of the same type.")

        query = query.insert(
            *[
                ValueWrapper(getattr(instance, f.name))
                for f in instance.__dataclass_fields__.values()
            ]
        )

    return str(query)


if __name__ == "__main__":
    students = [Student() for _ in range(5)]
    sql = generate_insert_query(students)
    print(sql)
