from mongo_data_generating.factories import faculty_factory
from mongo_data_generating.repositories import GenericRepository


def seed_data():
    faculty = faculty_factory()
    GenericRepository("faculties").insert_one(faculty)


if __name__ == "__main__":
    seed_data()
