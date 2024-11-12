from typing import Sequence, Callable

from data_generating.factories.models import *
from data_generating.factories.models import Course
from data_generating.seeders.utils import unique


def generate_users_seeder(
    num_records: int,
    degrees: list[Degree],
    administrator_percentage: float = 0.15,
    host_percentage: float = 0.35,
    student_percentage: float = 0.5,
) -> Sequence[User]:
    return unique(
        lambda: User(
            degree=random.choice(degrees).id,
            profile_type=random.choices(
                [0, 1, 2],
                weights=[administrator_percentage, host_percentage, student_percentage],
            )[0],
        ),
        num_records,
    )


def generate_faculty_seeder(num_records: int) -> Sequence[Faculty]:
    return [Faculty() for _ in range(num_records)]


def generate_faculty_administrator_seeder(
    num_records: int,
    faculties: Sequence[Faculty],
    administrators: Sequence[User],
) -> Sequence[FacultyAdministrator]:
    return unique(
        lambda: FacultyAdministrator(
            faculty_id=random.choice(faculties).id,
            administrator_id=random.choice(administrators).id,
        ),
        num_records,
    )


def generate_term_seeder(
    num_records: int, fields_of_study: Sequence[FieldOfStudy], creators: Sequence[User]
) -> Sequence[Term]:
    return [
        Term(
            field_of_study_id=random.choice(fields_of_study).id,
            created_by=random.choice(creators).id,
        )
        for _ in range(num_records)
    ]


def generate_field_of_study_seeder(
    num_records: int, faculties: Sequence[Faculty], creators: Sequence[User | None]
) -> Sequence[FieldOfStudy]:
    return [
        FieldOfStudy(
            faculty_id=random.choice(faculties).id,
            created_by=(
                random.choice(creators).id
                if random.choice(creators) is not None
                else None
            ),
        )
        for _ in range(num_records)
    ]


def generate_college_term_seeder(num_records: int) -> Sequence[CollegeTerm]:
    return [CollegeTerm() for _ in range(num_records)]


def generate_degree_seeder(num_records: int) -> Sequence[Degree]:
    return [Degree() for _ in range(num_records)]


def generate_group_seeder(
    num_records: int,
    courses: Sequence[Course],
    college_terms: Sequence[CollegeTerm],
    creators: Sequence[User | None],
) -> Sequence[Group]:
    return [
        Group(
            course_id=random.choice(courses).id,
            college_term_id=random.choice(college_terms).id,
            created_by=(
                random.choice(creators).id
                if random.choice(creators) is not None
                else None
            ),
        )
        for _ in range(num_records)
    ]


def generate_course_seeder(
    num_records: int,
    terms: Sequence[Term],
    creators_administrators: Sequence[User | None],
) -> Sequence[Course]:
    return [
        Course(
            term_id=random.choice(terms).id,
            created_by=random.choice(creators_administrators).id,
        )
        for _ in range(num_records)
    ]


def generate_student_group_seeder(
    num_records: int,
    groups: Sequence[Group],
    students: Sequence[User],
    creators: Sequence[User],
) -> Sequence[StudentGroup]:
    return unique(
        lambda: StudentGroup(
            group_id=random.choice(groups).id,
            student_id=random.choice(students).id,
            created_by=random.choice(creators).id,
        ),
        num_records,
    )


def generate_host_group_seeder(
    num_records: int, hosts: Sequence[User], groups: Sequence[Group]
) -> Sequence[HostGroup]:
    return unique(
        lambda: HostGroup(
            host_id=random.choice(hosts).id,
            group_id=random.choice(groups).id,
        ),
        num_records,
    )


def generate_host_course_seeder(
    num_records: int,
    hosts: Sequence[User],
    courses: Sequence[Course],
    creators: Sequence[User | None],
) -> Sequence[HostCourse]:
    return [
        HostCourse(
            host_id=random.choice(hosts).id,
            course_id=random.choice(courses).id,
            created_by=(
                random.choice(creators).id
                if random.choice(creators) is not None
                else None
            ),
        )
        for _ in range(num_records)
    ]


def generate_entry_seeder(
    num_records: int, groups: Sequence[Group | None], hosts: Sequence[User | None]
) -> Sequence[Entry]:
    return [
        Entry(
            group_id=(
                random.choice(groups).id if random.choice(groups) is not None else None
            ),
            host_id=(
                random.choice(hosts).id if random.choice(hosts) is not None else None
            ),
        )
        for _ in range(num_records)
    ]


def generate_comment_of_entry_seeder(
    num_records: int, commenters: Sequence[User], entries: Sequence[Entry]
) -> Sequence[CommentOfEntry]:
    return [
        CommentOfEntry(
            user_id=random.choice(commenters).id,
            entry_id=random.choice(entries).id,
        )
        for _ in range(num_records)
    ]


def generate_exercise_seeder(
    num_records: int, entries: Sequence[Entry]
) -> Sequence[Exercise]:
    return [Exercise(entry_id=random.choice(entries).id) for _ in range(num_records)]


def generate_entry_file_seeder(
    num_records: int, entries: Sequence[Entry]
) -> Sequence[EntryFile]:
    return [EntryFile(entry_id=random.choice(entries).id) for _ in range(num_records)]


def generate_solution_seeder(
    num_records: int, exercises: Sequence[Exercise], students: Sequence[User]
) -> Sequence[Solution]:
    return [
        Solution(
            exercise_id=random.choice(exercises).id,
            student_id=random.choice(students).id,
        )
        for _ in range(num_records)
    ]


def generate_solution_file_seeder(
    num_records: int, solutions: Sequence[Solution]
) -> Sequence[SolutionFile]:
    return [
        SolutionFile(solution_id=random.choice(solutions).id)
        for _ in range(num_records)
    ]


def generate_solution_comment_seeder(
    num_records: int,
    commenters: Sequence[User | None],
    solutions: Sequence[Solution],
) -> Sequence[SolutionComment]:
    return [
        SolutionComment(
            user_id=user.id if (user := random.choice(commenters)) else None,
            solution_id=random.choice(solutions).id,
        )
        for _ in range(num_records)
    ]


def generate_test_seeder(num_records: int, entries: Sequence[Entry]) -> Sequence[Test]:
    return [Test(entry_id=random.choice(entries).id) for _ in range(num_records)]


def generate_attempt_seeder(
    num_records: int, students: Sequence[User], tests: Sequence[Test]
) -> Sequence[Attempt]:
    return [
        Attempt(student_id=random.choice(students).id, test_id=random.choice(tests).id)
        for _ in range(num_records)
    ]


def generate_open_question_seeder(
    num_records: int, tests: Sequence[Test]
) -> Sequence[OpenQuestion]:
    return [OpenQuestion(test_id=random.choice(tests).id) for _ in range(num_records)]


def generate_closed_question_seeder(
    num_records: int, tests: Sequence[Test]
) -> Sequence[ClosedQuestion]:
    return [ClosedQuestion(test_id=random.choice(tests).id) for _ in range(num_records)]


def generate_choice_seeder(
    num_records: int, closed_questions: Sequence[ClosedQuestion]
) -> Sequence[Choice]:
    return [
        Choice(closed_question_id=random.choice(closed_questions).id)
        for _ in range(num_records)
    ]


def generate_closed_answer_seeder(
    num_records: int,
    attempts: Sequence[Attempt],
    closed_questions: Sequence[ClosedQuestion],
) -> Sequence[ClosedAnswer]:
    return [
        ClosedAnswer(
            attempt_id=random.choice(attempts).id,
            closed_question_id=random.choice(closed_questions).id,
        )
        for _ in range(num_records)
    ]


def generate_closed_answer_choice_seeder(
    num_records: int, closed_answers: Sequence[ClosedAnswer], choices: Sequence[Choice]
) -> Sequence[ClosedAnswerChoice]:
    return unique(
        lambda: ClosedAnswerChoice(
            closed_answer_id=random.choice(closed_answers).id,
            choice_id=random.choice(choices).id,
        ),
        num_records,
    )
