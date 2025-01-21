__all__ = [
    "FacultyAdministrator",
    "Course",
    "Term",
    "FieldOfStudy",
    "Faculty",
    "HostCourse",
    "User",
    "CollegeTerm",
    "Student",
    "Group",
    "Exercise",
    "Choice",
    "OpenQuestion",
    "ClosedQuestion",
    "Test",
    "CommentUser",
    "CommentOfEntry",
    "Entry",
    "SolutionComment",
    "Grade",
    "Solution",
    "ClosedAnswer",
    "OpenAnswer",
    "Attempt",
]

import random
from datetime import datetime
from typing import List

from bson import ObjectId
from pydantic import Field

from mongo_data_generating.models import fake
from mongo_data_generating.models.abstact import BaseModel, Question
from mongo_data_generating.models.mixins import TimestampMixin

# Faculty Schemas


class FacultyAdministrator(BaseModel):
    pass


class Course(BaseModel, TimestampMixin):
    title: str = Field(
        default_factory=lambda: " ".join(fake.words(random.randint(1, 4)))
    )
    description: str = Field(default_factory=fake.text)


class Term(BaseModel, TimestampMixin):
    term_number: int = Field(default_factory=lambda: fake.random_int(min=1, max=7))
    courses: List[Course] = Field()


class FieldOfStudy(BaseModel, TimestampMixin):
    name: str = Field(default_factory=fake.word)
    description: str = Field(
        default_factory=lambda: " ".join(fake.words(random.randint(5, 15)))
    )
    start_year: int = Field(default_factory=lambda: fake.random_int(min=2010, max=2025))
    terms: List[Term] = Field()


class Faculty(BaseModel):
    name: str = Field(default_factory=fake.word)
    email: str = Field(default_factory=fake.email)
    phone: str = Field(default_factory=fake.phone_number)
    website: str = Field(default_factory=fake.url)
    faculty_administrators: List[FacultyAdministrator] = Field()
    fields_of_study: List[FieldOfStudy] = Field()


# Users Schemas


class HostCourse(BaseModel, TimestampMixin):
    course_id: ObjectId = Field(default_factory=ObjectId)
    is_admin: bool = Field(
        default_factory=lambda: fake.boolean(chance_of_getting_true=20)
    )


class User(BaseModel):
    first_name: str = Field(default_factory=fake.first_name)
    last_name: str = Field(default_factory=fake.last_name)
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=lambda: fake.password(length=12))
    is_active: bool = Field(
        default_factory=lambda: random.choices([True, False], weights=[75, 25])[0]
    )
    degree: str | None = Field(
        default_factory=lambda: random.choice(["Bachelor", "Master", "PhD"])
    )
    profile_type: int = Field()  # 0 - administrator, 1 - host, 2 - student
    courses_hosted: List[HostCourse] = Field()
    groups_hosted: List[ObjectId] = Field()


class CollegeTerm(BaseModel):
    start_date: datetime = Field(default_factory=lambda: fake.date_time_this_year())
    end_date: datetime | None = Field(
        default_factory=lambda: fake.date_time_this_year()
    )

# Group Schemas


class Student(BaseModel):
    student_id: ObjectId = Field(default_factory=ObjectId)
    first_name: str = Field(default_factory=fake.first_name)
    last_name: str = Field(default_factory=fake.last_name)
    assigned_by: ObjectId = Field(default_factory=ObjectId)
    assigned_at: datetime = Field(default_factory=lambda: fake.date_time_this_year())


class Group(BaseModel, TimestampMixin):
    name: str = Field(default_factory=fake.word)
    description: str = Field(default_factory=fake.text)
    image: str | None = Field(default_factory=fake.url)
    college_term: CollegeTerm = Field()
    assigned_to_course_id: ObjectId | None = Field(default_factory=ObjectId)
    students: List[Student] = Field()


# Entries Schemas


class Exercise(BaseModel):
    exercise_id: ObjectId = Field(default_factory=ObjectId)
    due_date: datetime = Field(default_factory=lambda x: fake.date_time_this_year())


class Choice(BaseModel):
    designation: str = Field(default_factory=fake.word)
    content: str = Field(default_factory=fake.text)
    is_correct: bool | None = Field(default_factory=fake.boolean)


class OpenQuestion(Question):
    open_q_id: ObjectId = Field(default_factory=ObjectId)


class ClosedQuestion(Question):
    closed_q_id: ObjectId = Field(default_factory=ObjectId)
    choices: List[Choice] = Field()


class Test(BaseModel):
    test_id: ObjectId = Field(default_factory=ObjectId)
    title: str = Field(default_factory=fake.word)
    description: str = Field(default_factory=fake.text)
    available_from_date: datetime = Field(
        default_factory=lambda: fake.date_time_this_year()
    )
    available_to_date: datetime | None = Field(
        default_factory=lambda: fake.date_time_this_year()
    )
    max_seconds_for_open: int | None = Field(
        default_factory=lambda: fake.pyint(min_value=0, max_value=120)
    )
    max_seconds_for_closed: int | None = Field(
        default_factory=lambda: fake.pyint(min_value=0, max_value=120)
    )
    duration_in_minutes: int = Field(
        default_factory=lambda: fake.pyint(min_value=0, max_value=180)
    )
    closed_questions: List[ClosedQuestion] = Field()
    open_questions: List[OpenQuestion] = Field()


class CommentUser(BaseModel):
    user_id: ObjectId = Field(default_factory=ObjectId)
    first_name: str = Field(default_factory=fake.first_name)
    last_name: str = Field(default_factory=fake.last_name)


class CommentOfEntry(BaseModel):
    user: CommentUser = Field(default_factory=CommentUser)
    content: str = Field(default_factory=fake.text)
    created_at: datetime = Field(default_factory=lambda: fake.date_time_this_year())


class Entry(BaseModel, TimestampMixin):
    group_id: ObjectId = Field(default_factory=ObjectId)
    title: str = Field(default_factory=fake.word)
    updated_at: datetime = Field(default_factory=lambda: fake.date_time_this_year())
    content: str = Field(default_factory=fake.text)
    file_url: str | None = Field(default_factory=fake.url)
    exercise: Exercise | None = Field(default_factory=Exercise)
    test: Test | None = Field(default_factory=Test)
    comments: List[CommentOfEntry] = Field()


# Solution Schemas


class SolutionComment(BaseModel):
    commenter_id: ObjectId = Field(default_factory=ObjectId)
    content: str = Field(default_factory=fake.text)
    created_at: datetime = Field(default_factory=lambda: fake.date_time_this_year())


class Grade(BaseModel):
    value: float = Field(
        default_factory=lambda: random.choice([2.0, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5])
    )
    added_at: datetime = Field(default_factory=lambda: fake.date_time_this_year())
    added_by: ObjectId = Field(default_factory=ObjectId)


class Solution(BaseModel):
    student_id: ObjectId = Field(default_factory=ObjectId)
    exercise_id: ObjectId = Field(default_factory=ObjectId)
    file_url: str = Field(default_factory=fake.url)
    comments: List[SolutionComment] = Field()
    grade: Grade | None = Field()


# Attempt Schemas


class ClosedAnswer(BaseModel):
    closed_q_id: ObjectId = Field(default_factory=ObjectId)
    choice: str = Field(default_factory=fake.word)


class OpenAnswer(BaseModel):
    open_q_id: ObjectId = Field(default_factory=ObjectId)
    content: str = Field(default_factory=fake.text)
    points: int = Field(default_factory=lambda: fake.random_int(min=0, max=100))


class Attempt(BaseModel):
    student_id: ObjectId = Field(default_factory=ObjectId)
    test_id: ObjectId = Field(default_factory=ObjectId)
    score: float | None = Field(
        default_factory=lambda: fake.pyfloat(min_value=0, max_value=100)
    )
    grade: float = Field(
        default_factory=lambda x: random.choice([2.0, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5])
    )
    started_at: datetime = Field(default_factory=lambda: fake.date_time_this_year())
    submitted_at: datetime | None = Field(
        default_factory=lambda: fake.date_time_this_year()
    )
    answers_for_open_q: List[OpenAnswer] = Field()
    answers_for_closed_q: List[ClosedAnswer] = Field()


if __name__ == "__main__":
    # Faculty Schema Test
    courses = [Course() for _ in range(5)]
    t = Term(courses=courses)
    fos = FieldOfStudy(terms=[t])
    fa = FacultyAdministrator()
    f = Faculty(faculty_administrators=[fa], fields_of_study=[fos])
    print(f.model_dump_json(indent=4))

    # Users Schema Test
    hc = HostCourse()
    u = User(
        courses_hosted=[hc], groups_hosted=[ObjectId(), ObjectId()], profile_type=1
    )
    print(u.model_dump_json(indent=4))

    # Group Schema Test
    ct = CollegeTerm()
    s = [Student() for _ in range(5)]
    g = Group(college_term=ct, students=s)
    print(g.model_dump_json(indent=4))

    # Entry Schema Test
    c = ClosedQuestion(choices=[Choice() for _ in range(4)])
    o = OpenQuestion()
    t = Test(open_questions=[o], closed_questions=[c])
    e = Exercise()
    co = CommentOfEntry()
    entry = Entry(test=t, exercise=e, comments=[co])
    print(entry.model_dump_json(indent=4))

    # Solution Schema Test
    sc = SolutionComment()
    g = Grade()
    s = Solution(comments=[sc], grade=g)
    print(s.model_dump_json(indent=4))

    # Attempt Schema Test
    c = ClosedAnswer()
    o = OpenAnswer()
    a = Attempt(answers_for_open_q=[o], answers_for_closed_q=[c])
    print(a.model_dump_json(indent=4))
