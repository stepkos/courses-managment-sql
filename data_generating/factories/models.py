import random
from collections import OrderedDict
from dataclasses import dataclass, field
from typing import List, Sequence

from data_generating.factories import fake
from data_generating.factories.abstact import *
from data_generating.factories.utils import nullable_field, make_hashable


@dataclass(kw_only=True, frozen=True)
class User(BaseModel):
    _TABLE_NAME: str = "users"

    first_name: str = field(default_factory=fake.first_name)
    surname: str = field(default_factory=fake.last_name)
    email: str = field(default_factory=fake.email)
    password: str = field(default_factory=lambda: fake.password(length=12))
    is_active: bool = field(
        default_factory=lambda: random.choices([True, False], weights=[75, 25])[0]
    )
    degree: str | None
    profile_type: int # 0 - administrator, 1 - host, 2 - student

@dataclass(kw_only=True, frozen=True)
class Faculty(BaseModel):
    _TABLE_NAME: str = "faculties"

    name: str = field(default_factory=fake.word)
    email: str = field(default_factory=fake.email)
    phone: str = field(default_factory=fake.phone_number)
    website: str = field(default_factory=fake.url)


@dataclass(kw_only=True, frozen=True)
class FacultyAdministrator(BaseModel, make_hashable("faculty_id", "administrator_id")):
    _TABLE_NAME: str = "faculty_administrators"

    faculty_id: str
    administrator_id: str


@dataclass(kw_only=True, frozen=True)
class FieldOfStudy(BaseModel):
    _TABLE_NAME: str = "fields_of_study"

    name: str = field(default_factory=fake.word)
    faculty_id: str
    description: str = ""
    start_year: int = field(default_factory=lambda: fake.random_int(min=2010, max=2025))
    created_by: str | None
    created_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))


@dataclass(kw_only=True, frozen=True)
class Term(BaseModel):
    _TABLE_NAME: str = "terms"

    field_of_study_id: str
    term_number: int = field(
        default_factory=lambda: fake.random_int(min=1, max=15)
    )
    created_by: str | None
    created_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))


@dataclass(kw_only=True, frozen=True)
class Course(BaseModel):
    _TABLE_NAME: str = "courses"

    term_id: str
    title: str = field(default_factory=fake.name)
    description: str = field(default_factory=fake.text)
    created_by: str | None
    created_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))


@dataclass(kw_only=True, frozen=True)
class CollegeTerm(BaseModel):
    _TABLE_NAME: str = "college_terms"

    # TODO: definitely use better generators here
    start_date: str = field(default_factory=lambda: str(fake.date_time_this_year()))
    end_date: str | None = field(default_factory=lambda: str(fake.date_time_this_year()))


@dataclass(kw_only=True, frozen=True)
class Degree(BaseModel):
    _TABLE_NAME: str = "degrees"

    name: str = field(
        default_factory=lambda: fake.random_element(
            elements=OrderedDict([("mgr", 0.75), ("dr", 0.2), ("prof", 0.05)])
        )
    )


@dataclass(kw_only=True, frozen=True)
class Group(BaseModel):
    _TABLE_NAME: str = "groups"

    course_id: str
    college_term_id: str
    name: str = field(default_factory=fake.word)
    description: str = field(default_factory=fake.text)
    image: str | None = field(default_factory=nullable_field(fake.url))
    created_by: str | None
    created_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))


@dataclass(kw_only=True, frozen=True)
class StudentGroup(BaseModel, make_hashable("group_id", "student_id")):
    _TABLE_NAME: str = "student_groups"

    group_id: str
    student_id: str
    created_by: str
    created_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))


@dataclass(kw_only=True, frozen=True)
class HostGroup(BaseModel, make_hashable("host_id", "group_id")):
    _TABLE_NAME: str = "host_groups"

    host_id: str
    group_id: str


@dataclass(kw_only=True, frozen=True)
class HostCourse(BaseModel):
    _TABLE_NAME: str = "host_courses"

    host_id: str
    course_id: str
    is_course_admin: bool = field(
        default_factory=lambda: fake.boolean(chance_of_getting_true=20)
    )
    created_by: str | None
    created_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))


@dataclass(kw_only=True, frozen=True)
class Entry(BaseModel):
    _TABLE_NAME: str = "entries"

    group_id: str | None
    title: str = field(default_factory=fake.word)
    created_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))
    updated_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))
    content: str = field(default_factory=fake.text)
    host_id: str | None


@dataclass(kw_only=True, frozen=True)
class CommentOfEntry(BaseModel):
    _TABLE_NAME: str = "comment_of_entries"

    user_id: str
    content: str = field(default_factory=fake.text)
    created_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))
    entry_id: str


@dataclass(kw_only=True, frozen=True)
class EntryFile(File):
    _TABLE_NAME: str = "entry_files"

    entry_id: str


@dataclass(kw_only=True, frozen=True)
class Exercise(BaseModel):
    _TABLE_NAME: str = "exercises"

    entry_id: str
    due_date: str | None = field(
        default_factory=nullable_field(lambda: str(fake.date_time_this_year()))
    )


@dataclass(kw_only=True, frozen=True)
class Solution(BaseModel):
    _TABLE_NAME: str = "solutions"

    exercise_id: str
    student_id: str
    grade: float = field(
        default_factory=lambda: fake.pyfloat(min_value=0, max_value=10)
    )
    submitted_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))
    text_answer: str = field(default_factory=fake.text)


@dataclass(kw_only=True, frozen=True)
class SolutionFile(File):
    _TABLE_NAME: str = "solution_files"

    solution_id: str


@dataclass(kw_only=True, frozen=True)
class SolutionComment(BaseModel):
    _TABLE_NAME: str = "solution_comments"

    user_id: str | None
    solution_id: str
    content: str = field(default_factory=fake.text)
    created_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))


@dataclass(kw_only=True, frozen=True)
class Test(BaseModel):
    _TABLE_NAME: str = "tests"

    entry_id: str
    title: str = field(default_factory=fake.word)
    description: str = field(default_factory=fake.text)
    available_from_date: str = field(
        default_factory=lambda: str(fake.date_time_this_year())
    )
    available_to_date: str | None = field(
        default_factory=nullable_field(lambda: str(fake.date_time_this_year()))
    )
    max_seconds_for_open: int | None = field(
        default_factory=nullable_field(lambda: fake.pyint(min_value=0, max_value=120))
    )
    max_seconds_for_closed: int | None = field(
        default_factory=nullable_field(lambda: fake.pyint(min_value=0, max_value=120))
    )
    duration_in_minutes: int = field(default_factory=lambda: fake.pyint(min_value=0))
    created_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))
    updated_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))


@dataclass(kw_only=True, frozen=True)
class Attempt(BaseModel):
    _TABLE_NAME: str = "attempts"

    student_id: str
    test_id: str
    score: float | None = field(
        default_factory=lambda: fake.pyfloat(min_value=0, max_value=100)
    )
    started_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))
    submitted_at: str | None = field(
        default_factory=nullable_field(lambda: str(fake.date_time_this_year()))
    )


@dataclass(kw_only=True, frozen=True)
class OpenQuestion(Question):
    _TABLE_NAME: str = "open_questions"

    test_id: str


@dataclass(kw_only=True, frozen=True)
class ClosedQuestion(Question):
    _TABLE_NAME: str = "closed_questions"

    test_id: str
    is_multiple: bool = field(default_factory=fake.boolean)


@dataclass(kw_only=True, frozen=True)
class Choice(BaseModel):
    _TABLE_NAME: str = "choices"

    closed_question_id: str
    content: str = field(default_factory=fake.text)
    is_correct: bool | None = field(default_factory=nullable_field(fake.boolean))


@dataclass(kw_only=True, frozen=True)
class ClosedAnswer(BaseModel):
    _TABLE_NAME: str = "closed_answers"

    attempt_id: str
    closed_question_id: str
    submitted_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))


@dataclass(kw_only=True, frozen=True)
class ClosedAnswerChoice(BaseModel, make_hashable("closed_answer_id", "choice_id")):
    _TABLE_NAME: str = "closed_answer_choices"

    closed_answer_id: str
    choice_id: str


@dataclass(kw_only=True, frozen=True)
class OpenAnswer(BaseModel):
    _TABLE_NAME: str = "open_answers"

    open_question_id: str
    content: str = field(default_factory=fake.text)
    attempt_id: str
    submitted_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))


def generate_open_answer_seeder(
    num_records: int, open_question: List[OpenQuestion], attempts: List[Attempt]
) -> List[OpenAnswer]:
    return [
        OpenAnswer(
            open_question_id=random.choice(open_question).id,
            attempt_id=random.choice(attempts).id,
        )
        for _ in range(num_records)
    ]
