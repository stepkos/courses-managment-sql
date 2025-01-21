import random

from bson import ObjectId

from mongo_data_generating.models.models import *


def faculty_factory() -> Faculty:
    field_of_studies = []
    for _ in range(random.randint(1, 10)):
        terms = []
        for _ in range(random.randint(1, 10)):
            courses = [Course() for _ in range(random.randint(1, 7))]
            terms.append(Term(courses=courses))

        field_of_studies.append(FieldOfStudy(terms=terms))

    faculty_administrators = [
        FacultyAdministrator()
        for _ in range(random.randint(1, 3))
    ]
    faculty = Faculty(
        faculty_administrators=faculty_administrators,
        fields_of_study=field_of_studies
    )
    return faculty


def user_factory() -> User:
    courses_hosted = [
        HostCourse()
        for _ in range(random.randint(1, 10))
    ]
    groups_hosted = [
        ObjectId()
        for _ in range(random.randint(1, 10))
    ]
    user = User(
        courses_hosted=courses_hosted,
        groups_hosted=groups_hosted,
        profile_type=random.randint(0, 2)
    )
    return user


def group_factory() -> Group:
    students = [
        Student()
        for _ in range(random.randint(1, 10))
    ]
    group = Group(
        college_term=CollegeTerm(),
        students=students
    )
    return group


def entry_factory() -> Entry:
    open_questions = [
        OpenQuestion()
        for _ in range(random.randint(1, 10))
    ]
    closed_questions = [
        ClosedQuestion(choices=[Choice() for _ in range(4)])
        for _ in range(random.randint(1, 10))
    ]
    test = Test(
        open_questions=open_questions,
        closed_questions=closed_questions
    )
    exercise = Exercise()
    comments = [
        CommentOfEntry()
        for _ in range(random.randint(1, 10))
    ]
    entry = Entry(
        test=test,
        exercise=exercise,
        comments=comments
    )
    return entry


def solution_factory() -> Solution:
    comments = [
        SolutionComment()
        for _ in range(random.randint(1, 10))
    ]
    grade = Grade()
    solution = Solution(
        comments=comments,
        grade=grade
    )
    return solution


def attempt_factory() -> Attempt:
    answers_for_open_q = [
        OpenAnswer()
        for _ in range(random.randint(1, 10))
    ]
    answers_for_closed_q = [
        ClosedAnswer()
        for _ in range(random.randint(1, 10))
    ]
    attempt = Attempt(
        answers_for_open_q=answers_for_open_q,
        answers_for_closed_q=answers_for_closed_q
    )
    return attempt
