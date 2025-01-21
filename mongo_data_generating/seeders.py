from mongo_data_generating.factories import (
    attempt_factory,
    entry_factory,
    faculty_factory,
    group_factory,
    solution_factory,
    user_factory,
)
from mongo_data_generating.repositories import GenericRepository


def seed_data(multi: int = 1):
    faculty = faculty_factory()
    GenericRepository("faculties").insert_one(faculty)

    users = (user_factory() for _ in range(2000 * multi))
    GenericRepository("users").insert_many(users)

    groups = (group_factory() for _ in range(50 * multi))
    GenericRepository("groups").insert_many(groups)

    entries = (entry_factory() for _ in range(100 * multi))
    GenericRepository("entries").insert_many(entries)

    solutions = (solution_factory() for _ in range(100 * multi))
    GenericRepository("solutions").insert_many(solutions)

    attempts = (attempt_factory() for _ in range(100 * multi))
    GenericRepository("attempts").insert_many(attempts)


if __name__ == "__main__":
    seed_data()
