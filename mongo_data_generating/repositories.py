from typing import Iterable

from bson import ObjectId

from mongo_data_generating.models.models import *
from mongo_data_generating.clients import mongo_client_ctx


class GenericRepository:
    DB_NAME = "courses-managment"

    def __init__(self, schema_name: str):
        self.schema_name = schema_name

    def insert_one(self, instance: BaseModel):
        with mongo_client_ctx() as client:
            db = client[self.DB_NAME]
            collection = db[self.schema_name]
            return collection.insert_one(
                instance.model_dump(by_alias=True)
            )

    def insert_many(self, instances: Iterable[BaseModel]):
        with mongo_client_ctx() as client:
            db = client[self.DB_NAME]
            collection = db[self.schema_name]
            return collection.insert_many(
                map(lambda x: x.model_dump(by_alias=True), instances)
            )


if __name__ == "__main__":

    # Faculty test
    courses = [Course() for _ in range(5)]
    t = Term(courses=courses)
    fos = FieldOfStudy(terms=[t])
    fa = FacultyAdministrator()
    f = Faculty(
        faculty_administrators=[fa],
        fields_of_study=[fos]
    )
    GenericRepository("faculties").insert_one(f)

    # User test
    hc = HostCourse()
    u = User(
        courses_hosted=[hc],
        groups_hosted=[ObjectId(), ObjectId()],
        profile_type=1
    )
    GenericRepository("users").insert_one(u)
