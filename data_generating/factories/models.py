import random
from dataclasses import dataclass, field

from data_generating.factories import fake
from data_generating.factories.abstact import *
from data_generating.factories.utils import nullable_field
from collections import OrderedDict


@dataclass(kw_only=True)
class Administrator(User):
    _TABLE_NAME: str = "administrators"


@dataclass(kw_only=True)
class Faculty(BaseModel):
    _TABLE_NAME: str = "faculties"

    name: str = field(default_factory=fake.name)  # TODO: use better generator
    email: str = field(default_factory=fake.email)
    phone: str = field(default_factory=fake.phone_number)
    website: str = field(default_factory=fake.url)


@dataclass(kw_only=True)
class FacultyAdministrator(BaseModel):
    _TABLE_NAME: str = "faculty_administrators"

    faculty_id: int
    administrator_id: int


@dataclass(kw_only=True)
class FieldOfStudy(BaseModel):
    _TABLE_NAME: str = "fields_of_study"

    name: str = field(default_factory=fake.name)  # TODO: use better generator
    faculty_id: int
    description: str = ""
    start_year: int = field(default_factory=lambda: fake.random_int(min=2010, max=2025))
    created_by: int | None
    created_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))


@dataclass(kw_only=True)
class Term(BaseModel):
    _TABLE_NAME: str = "terms"

    field_of_study_id: int
    term_number: int = field(
        default_factory=lambda: fake.random_int(min=1, max=10)
    )  # TODO: is 10 really the max? What about phds?
    created_by: int | None
    created_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))


@dataclass(kw_only=True)
class Course(BaseModel):
    _TABLE_NAME: str = "courses"

    term_id: int
    title: str = field(default_factory=fake.name)  # TODO: use better generator
    description: str = field(default_factory=fake.text)  # TODO?: use better generator
    created_by: int | None
    created_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))


@dataclass(kw_only=True)
class CollegeTerm(BaseModel):
    _TABLE_NAME: str = "college_terms"

    # TODO: definitely use better generators here
    start_date: str = field(default_factory=lambda: str(fake.date_time_this_year))
    end_date: str | None = field(default_factory=lambda: str(fake.date_time_this_year))


@dataclass(kw_only=True)
class Degree(BaseModel):
    _TABLE_NAME: str = "degrees"

    name: str = field(
        default_factory=lambda: fake.random_element(
            elements=OrderedDict([("mgr", 0.75), ("dr", 0.2), ("prof", 0.05)])
        )
    )


@dataclass(kw_only=True)
class Host(User):
    _TABLE_NAME: str = "hosts"

    degree: str | None


@dataclass(kw_only=True)
class Group(BaseModel):
    _TABLE_NAME: str = "groups"

    course_id: int
    college_term_id: int
    name: str = field(default_factory=fake.name)  # TODO: use better generator
    description: str = field(default_factory=fake.name)  # TODO: use better generator
    image: str | None = field(default_factory=nullable_field(fake.url))
    created_by: int | None
    created_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))


@dataclass(kw_only=True)
class Student(User):
    _TABLE_NAME: str = "students"

    index: str = field(
        default_factory=lambda: str(fake.random_int(min=100000, max=999999))
    )


@dataclass(kw_only=True)
class StudentGroup(BaseModel):
    _TABLE_NAME: str = "student_groups"

    group_id: int
    student_id: int
    created_by: int
    created_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))


@dataclass(kw_only=True)
class HostGroup(BaseModel):
    _TABLE_NAME: str = "host_groups"

    host_id: int
    group_id: int


@dataclass(kw_only=True)
class HostCourse(BaseModel):
    _TABLE_NAME: str = "host_courses"

    host_id: int
    course_id: int
    is_course_admin: bool = field(
        default_factory=lambda: fake.boolean(chance_of_getting_true=20)
    )
    created_by: int | None
    created_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))


@dataclass(kw_only=True)
class Entry(BaseModel):
    _TABLE_NAME: str = "entries"

    group_id: str | None
    title: str = field(default_factory=fake.word)
    created_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))
    updated_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))
    content: str = field(default_factory=fake.text)
    host_id: int | None


@dataclass(kw_only=True)
class CommentOfEntry(BaseModel):
    _TABLE_NAME: str = "comment_of_entries"

    commenter_id: int
    commenter_type: int
    content: str = field(default_factory=fake.text)
    created_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))
    entry_id: int


@dataclass(kw_only=True)
class EntryFile(File):
    _TABLE_NAME: str = "entry_files"

    entry_id: int


@dataclass(kw_only=True)
class Exercise(BaseModel):
    _TABLE_NAME: str = "exercises"

    entry_id: int
    due_date: str | None = field(
        default_factory=nullable_field(lambda: str(fake.date_time_this_year()))
    )


@dataclass(kw_only=True)
class Solution(BaseModel):
    _TABLE_NAME: str = "solutions"

    exercise_id: int
    student_id: int
    grade: float = field(
        default_factory=lambda: fake.pyfloat(min_value=0, max_value=10)
    )
    submitted_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))
    text_answer: str = field(default_factory=fake.text)


@dataclass(kw_only=True)
class SolutionFile(File):
    _TABLE_NAME: str = "solution_files"

    solution_id: int


@dataclass(kw_only=True)
class SolutionComment(BaseModel):
    _TABLE_NAME: str = "solution_comments"

    commenter_id: int | None
    commenter_type: int | None
    solution_id: int
    content: str = field(default_factory=fake.text)
    created_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))


@dataclass(kw_only=True)
class Test(BaseModel):
    _TABLE_NAME: str = "tests"

    entry_id: int
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


@dataclass(kw_only=True)
class Attempt(BaseModel):
    _TABLE_NAME: str = "attempts"

    student_id: int
    test_id: int
    score: float | None = field(
        default_factory=lambda: fake.pyfloat(min_value=0, max_value=100)
    )
    started_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))
    submitted_at: str | None = field(
        default_factory=nullable_field(lambda: str(fake.date_time_this_year))
    )


@dataclass(kw_only=True)
class OpenQuestion(BaseModel):
    _TABLE_NAME: str = "open_questions"

    test_id: int


@dataclass(kw_only=True)
class ClosedQuestion(BaseModel):
    _TABLE_NAME: str = "closed_questions"

    test_id: int
    is_multiple: bool = field(default_factory=fake.boolean)


@dataclass(kw_only=True)
class Choice(BaseModel):
    _TABLE_NAME: str = "choices"

    closed_question_id: int
    content: str = field(default_factory=fake.text)
    is_correct: bool | None = field(default_factory=nullable_field(fake.boolean))


@dataclass(kw_only=True)
class ClosedAnswer(BaseModel):
    _TABLE_NAME: str = "closed_answers"

    attempt_id: int
    closed_question_id: int
    submitted_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))


@dataclass(kw_only=True)
class ClosedAnswerChoice(BaseModel):
    _TABLE_NAME: str = "closed_answer_choices"

    closed_answer_id: int
    choice_id: int


@dataclass(kw_only=True)
class OpenAnswer(BaseModel):
    _TABLE_NAME: str = "open_answers"

    open_question_id: int
    content: str = field(default_factory=fake.text)
    attempt_id: int
    submitted_at: str = field(default_factory=lambda: str(fake.date_time_this_year()))
