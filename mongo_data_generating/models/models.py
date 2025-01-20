import random
from collections import OrderedDict
from typing import List, Sequence

from datetime import datetime, timedelta

from pydantic import Field

from data_generating.factories import fake
from data_generating.factories.abstact import BaseModel, File, Question, Answer
from mongo_data_generating.models.utils import nullable_factory, generate_submission_time


class User(BaseModel):
    first_name: str = Field(default_factory=fake.first_name)
    surname: str = Field(default_factory=fake.last_name)
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=lambda: fake.password(length=12))
    is_active: bool = Field(
        default_factory=lambda: random.choices([True, False], weights=[75, 25])[0]
    )
    degree: str | None
    profile_type: int  # 0 - administrator, 1 - host, 2 - student


class Faculty(BaseModel):
    name: str = Field(default_factory=fake.word)
    email: str = Field(default_factory=fake.email)
    phone: str = Field(default_factory=fake.phone_number)
    website: str = Field(default_factory=fake.url)


class FacultyAdministrator(BaseModel):
    faculty_id: str
    administrator_id: str


class FieldOfStudy(BaseModel):
    name: str = Field(default_factory=fake.word)
    faculty_id: str
    description: str = Field(default_factory=lambda: ' '.join(fake.words(random.randint(5, 15))))
    start_year: int = Field(default_factory=lambda: fake.random_int(min=2010, max=2025))
    created_by: str | None
    created_at: str = Field(default_factory=lambda: str(fake.date_time_this_year()))


class Term(BaseModel):
    Field_of_study_id: str
    term_number: int = Field(default_factory=lambda: fake.random_int(min=1, max=7))
    created_by: str | None
    created_at: str = Field(default_factory=lambda: str(fake.date_time_this_year()))


class Course(BaseModel):
    term_id: str
    title: str = Field(default_factory=lambda: ' '.join(fake.words(random.randint(1, 4))))
    description: str = Field(default_factory=fake.text)
    created_by: str | None
    created_at: str = Field(default_factory=lambda: str(fake.date_time_this_year()))


class CollegeTerm(BaseModel):
    # TODO: definitely use better generators here
    start_date: str = Field(default_factory=lambda: str(fake.date_time_this_year()))
    end_date: str | None = Field(
        default_factory=lambda: str(fake.date_time_this_year())
    )


class Degree(BaseModel):
    name: str  # "inz", "mgr", "dr", "prof"


class Group(BaseModel):
    course_id: str
    college_term_id: str
    name: str = Field(default_factory=fake.word)
    description: str = Field(default_factory=fake.text)
    image: str | None = Field(default_factory=nullable_factory(fake.url))
    created_by: str | None
    created_at: str = Field(default_factory=lambda: str(fake.date_time_this_year()))


class StudentGroup(BaseModel):
    group_id: str
    student_id: str
    created_by: str
    created_at: str = Field(default_factory=lambda: str(fake.date_time_this_year()))


class HostGroup(BaseModel):
    host_id: str
    group_id: str


class HostCourse(BaseModel):
    host_id: str
    course_id: str
    is_course_admin: bool = Field(
        default_factory=lambda: fake.boolean(chance_of_getting_true=20)
    )
    created_by: str | None
    created_at: str = Field(default_factory=lambda: str(fake.date_time_this_year()))


class Entry(BaseModel):
    group_id: str | None
    title: str = Field(default_factory=fake.word)
    created_at: str = Field(default_factory=lambda: str(fake.date_time_this_year()))
    updated_at: str = Field(default_factory=lambda: str(fake.date_time_this_year()))
    content: str = Field(default_factory=fake.text)
    host_id: str | None


class CommentOfEntry(BaseModel):
    user_id: str
    content: str = Field(default_factory=fake.text)
    created_at: str = Field(default_factory=lambda: str(fake.date_time_this_year()))
    entry_id: str


class EntryFile(File):
    entry_id: str


class Exercise(BaseModel):
    entry_id: str
    due_date: str | None = Field(
        default_factory=nullable_factory(lambda: str(fake.date_time_this_year()))
    )


class Solution(BaseModel):
    exercise_id: str
    student_id: str
    grade: float = Field(
        default_factory=lambda: random.choice([2.0, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5])
    )
    submitted_at: str = Field(default_factory=lambda: str(fake.date_time_this_year()))  
    text_answer: str = Field(default_factory=fake.text)


class SolutionFile(File):
    solution_id: str


class SolutionComment(BaseModel):
    user_id: str | None
    solution_id: str
    content: str = Field(default_factory=fake.text)
    created_at: str = Field(default_factory=lambda: str(fake.date_time_this_year()))


class Test(BaseModel):
    entry_id: str
    title: str = Field(default_factory=fake.word)
    description: str = Field(default_factory=fake.text)
    available_from_date: str = Field(
        default_factory=lambda: str(fake.date_time_this_year())
    )
    available_to_date: str | None = Field(
        default_factory=nullable_factory(lambda: str(fake.date_time_this_year()))
    )
    max_seconds_for_open: int | None = Field(
        default_factory=nullable_factory(lambda: fake.pyint(min_value=0, max_value=120))
    )
    max_seconds_for_closed: int | None = Field(
        default_factory=nullable_factory(lambda: fake.pyint(min_value=0, max_value=120))
    )
    duration_in_minutes: int = Field(default_factory=lambda: fake.pyint(min_value=0, max_value=180))
    created_at: str = Field(default_factory=lambda: str(fake.date_time_this_year()))
    updated_at: str = Field(default_factory=lambda: str(fake.date_time_this_year()))


class Attempt(BaseModel):
    student_id: str
    test_id: str
    score: float | None = Field(
        default_factory=lambda: fake.pyfloat(min_value=0, max_value=100)
    )
    started_at: str = Field(default_factory=lambda: str(fake.date_time_this_year()))
    submitted_at: str | None = Field(
        default_factory=lambda: generate_submission_time(datetime.fromisoformat(str(fake.date_time_this_year())))
    )

    def __post_init__(self):
        # Jeśli submitted_at jest None, ustaw score na 0
        if self.submitted_at is None:
            object.__setattr__(self, 'score', 0.0)


class OpenQuestion(Question):
    test_id: str


class ClosedQuestion(Question):
    test_id: str
    is_multiple: bool = Field(default_factory=fake.boolean)


class Choice(BaseModel):
    closed_question_id: str
    content: str = Field(default_factory=fake.text)
    is_correct: bool | None = Field(default_factory=lambda: nullable_factory(fake.boolean))


class ClosedAnswer(Answer):
    attempt_id: str
    closed_question_id: str
    submitted_at: str = Field(default_factory=lambda: str(fake.date_time_this_year()))


class ClosedAnswerChoice(BaseModel):
    closed_answer_id: str
    choice_id: str


class OpenAnswer(Answer):
    open_question_id: str
    content: str = Field(default_factory=fake.text)
    attempt_id: str
    submitted_at: str = Field(default_factory=lambda: str(fake.date_time_this_year()))

