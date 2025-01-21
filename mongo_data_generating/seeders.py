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
    res = faculty_factory()
    faculty = res["faculty"]
    courses_ids = res["all_courses_ids"]

    users = [user_factory(courses_ids) for _ in range(2000 * multi)]
    users_ids = [user.id for user in users]

    groups = [group_factory(courses_ids) for _ in range(50 * multi)]
    groups_ids = [group.id for group in groups]
    students_ids = []
    for group in groups:
        students_ids.extend([s.student_id for s in group.students])

    entries = [entry_factory(users_ids, groups_ids) for _ in range(100 * multi)]
    exercises_ids = [entry.exercise.exercise_id for entry in entries]
    tests_ids = [entry.test.test_id for entry in entries]

    solutions = [
        solution_factory(users_ids, students_ids, exercises_ids) for _ in range(100 * multi)
    ]

    attempts = [
        attempt_factory(students_ids, tests_ids)
        for _ in range(100 * multi)
    ]

    GenericRepository("faculties").insert_one(faculty)
    GenericRepository("users").insert_many(users)
    GenericRepository("groups").insert_many(groups)
    GenericRepository("entries").insert_many(entries)
    GenericRepository("solutions").insert_many(solutions)
    GenericRepository("attempts").insert_many(attempts)


if __name__ == "__main__":
    seed_data(5)
