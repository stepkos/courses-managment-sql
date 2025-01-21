from bson import ObjectId
from pydantic_mongo import AbstractRepository

from mongo_data_generating.models.models import *
from mongo_data_generating.clients import mongo_client_ctx


class FacultyRepository(AbstractRepository[Faculty]):
    class Meta:
        collection_name = 'faculties'


if __name__ == "__main__":

    with mongo_client_ctx() as client:
        db = client['courses-managment']
        faculties_collection = db['faculties']
        courses = [Course() for _ in range(5)]
        t = Term(courses=courses)
        fos = FieldOfStudy(terms=[t])
        fa = FacultyAdministrator()
        f = Faculty(
            faculty_administrators=[fa],
            fields_of_study=[fos]
        )

        d = f.model_dump(by_alias=True)
        print(d)
        faculties_collection.insert_one(d)
