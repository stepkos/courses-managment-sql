import random

from bson import ObjectId

from mongo_data_generating.models.models import *


def faculty_factory() -> dict:
    all_courses_ids = []
    field_of_studies = []
    for _ in range(random.randint(1, 10)):
        terms = []
        for _ in range(random.randint(1, 10)):
            courses = [Course() for _ in range(random.randint(1, 7))]
            terms.append(Term(courses=courses))
            all_courses_ids.extend([course.id for course in courses])

        field_of_studies.append(FieldOfStudy(terms=terms))

    faculty_administrators = [
        FacultyAdministrator() for _ in range(random.randint(1, 3))
    ]
    faculty = Faculty(
        faculty_administrators=faculty_administrators, fields_of_study=field_of_studies
    )
    return {
        "faculty": faculty,
        "all_courses_ids": all_courses_ids,
    }


def user_factory(
    courses_ids: list[ObjectId],
) -> User:
    courses_hosted = [
        HostCourse(course_id=random.choice(courses_ids))
        for _ in range(random.randint(1, 10))
    ]
    groups_hosted = [ObjectId() for _ in range(random.randint(1, 10))]
    user = User(
        courses_hosted=courses_hosted,
        groups_hosted=groups_hosted,
        profile_type=random.randint(0, 2),
    )
    return user


def group_factory(courses_ids: list[ObjectId]) -> Group:
    students = [Student() for _ in range(random.randint(1, 10))]
    group = Group(
        college_term=CollegeTerm(),
        students=students,
        assigned_to_course_id=random.choice(courses_ids),
    )
    return group


def entry_factory(
    users_ids: list[ObjectId],
    groups_ids: list[ObjectId],
) -> Entry:
    open_questions = [OpenQuestion() for _ in range(random.randint(1, 10))]
    closed_questions = [
        ClosedQuestion(choices=[Choice() for _ in range(4)])
        for _ in range(random.randint(1, 10))
    ]
    test = Test(open_questions=open_questions, closed_questions=closed_questions)
    exercise = Exercise()
    comments = [
        CommentOfEntry(user=CommentUser(user_id=random.choice(users_ids)))
        for _ in range(random.randint(1, 10))
    ]
    entry = Entry(
        test=test,
        exercise=exercise,
        comments=comments,
        group_id=random.choice(groups_ids),
    )
    return entry


def solution_factory(
    users_ids: list[ObjectId],
    students_ids: list[ObjectId],
    exercises_ids: list[ObjectId],
) -> Solution:
    comments = [
        SolutionComment(commenter_id=random.choice(users_ids))
        for _ in range(random.randint(1, 10))
    ]
    grade = Grade()
    solution = Solution(
        student_id=random.choice(students_ids),
        comments=comments,
        grade=grade,
        exercise_id=random.choice(exercises_ids),
    )
    return solution


def attempt_factory() -> Attempt:
    answers_for_open_q = [OpenAnswer() for _ in range(random.randint(1, 10))]
    answers_for_closed_q = [ClosedAnswer() for _ in range(random.randint(1, 10))]
    attempt = Attempt(
        answers_for_open_q=answers_for_open_q, answers_for_closed_q=answers_for_closed_q
    )
    return attempt
