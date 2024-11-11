from typing import List

from data_generating.factories.models import *
from data_generating.factories.models import Course


def generate_administrator_seeder(num_records: int) -> List[Administrator]:
    return [Administrator() for _ in range(num_records)]


def generate_faculty_seeder(num_records: int) -> List[Faculty]:
    return [Faculty() for _ in range(num_records)]


def generate_faculty_administrator_seeder(num_records: int, faculties: List[Faculty], administrators: List[Administrator]) -> List[FacultyAdministrator]:
    return [
        FacultyAdministrator(
            faculty_id=random.choice(faculties).id,
            administrator_id=random.choice(administrators).id
        )
        for _ in range(num_records)
    ]


def generate_field_of_study_seeder(num_records: int, faculties: List[Faculty], creators: List[User | None]) -> List[FieldOfStudy]:
    return [
        FieldOfStudy(
            faculty_id=random.choice(faculties).id,
            created_by=random.choice(creators).id if random.choice(creators) is not None else None,
        )
        for _ in range(num_records)
    ]

def generate_college_term_seeder(num_records: int) -> List[CollegeTerm]:
    return [CollegeTerm() for _ in range(num_records)]


def generate_degree_seeder(num_records: int) -> List[Degree]:
    return [Degree() for _ in range(num_records)]


def generate_host_seeder(num_records: int, degrees: List[Degree | None]) -> List[Host]:
    return [
        Host(degree=random.choice(degrees).name if random.choice(degrees) is not None else None)
        for _ in range(num_records)
    ]


def generate_group_seeder(num_records: int, courses: List[Course], college_terms: List[CollegeTerm], creators: List[User | None]) -> List[Group]:
    return [
        Group(
            course_id=random.choice(courses).id,
            college_term_id=random.choice(college_terms).id,
            created_by=random.choice(creators).id if random.choice(creators) is not None else None
        )
        for _ in range(num_records)
    ]

def generate_student_seeder(num_records: int) -> List[Student]:
    return [Student() for _ in range(num_records)]


def generate_student_group_seeder(num_records: int, groups: List[Group], students: List[Student], creators: List[User]) -> List[StudentGroup]:
    return [
        StudentGroup(
            group_id=random.choice(groups).id,
            student_id=random.choice(students).id,
            created_by=random.choice(creators).id
        )
        for _ in range(num_records)
    ]

def generate_host_course_seeder(num_records: int, hosts: List[Host], courses: List[Course], creators: List[User | None]) -> List[HostCourse]:
    return [
        HostCourse(
            host_id=random.choice(hosts).id,
            course_id=random.choice(courses).id,
            created_by=random.choice(creators).id if random.choice(creators) is not None else None
        )
        for _ in range(num_records)
    ]


def generate_entry_seeder(num_records: int, groups: List[Group | None], hosts: List[Host | None]) -> List[Entry]:
    return [
        Entry(
            group_id=random.choice(groups).id if random.choice(groups) is not None else None,
            host_id=random.choice(hosts).id if random.choice(hosts) is not None else None
        )
        for _ in range(num_records)
    ]


def generate_comment_of_entry_seeder(num_records: int, commenters: List[User], entries: List[Entry], commenter_types: List[int]) -> List[CommentOfEntry]:
    return [
        CommentOfEntry(
            commenter_id=random.choice(commenters).id,
            commenter_type=random.choice(commenter_types),
            entry_id=random.choice(entries).id
        )
        for _ in range(num_records)
    ]


def generate_exercise_seeder(num_records: int, entries: List[Entry]) -> List[Exercise]:
    return [
        Exercise(
            entry_id=random.choice(entries).id
        )
        for _ in range(num_records)
    ]


def generate_entry_file_seeder(num_records: int, entries: List[Entry]) -> List[EntryFile]:
    return [
        EntryFile(
            entry_id=random.choice(entries).id
        )
        for _ in range(num_records)
    ]


def generate_solution_seeder(num_records: int, exercises: List[Exercise], students: List[Student]) -> List[Solution]:
    return [
        Solution(
            exercise_id=random.choice(exercises).id,
            student_id=random.choice(students).id
        )
        for _ in range(num_records)
    ]


def generate_solution_file_seeder(num_records: int, solutions: List[Solution]) -> List[SolutionFile]:
    return [
        SolutionFile(
            solution_id=random.choice(solutions).id
        )
        for _ in range(num_records)
    ]


def generate_solution_comment_seeder(num_records: int, commenters: List[User | None], commenter_types: List[int | None], solutions: List[Solution]) -> List[SolutionComment]:
    return [
        SolutionComment(
            commenter_id=random.choice(commenters).id if random.choice(commenters) is not None else None,
            commenter_type=random.choice(commenter_types),
            solution_id=random.choice(solutions).id
        )
        for _ in range(num_records)
    ]


def generate_test_seeder(num_records: int, entries: List[Entry]) -> List[Test]:
    return [
        Test(
            entry_id=random.choice(entries).id
        )
        for _ in range(num_records)
    ]


def generate_attempt_seeder(num_records: int, students: List[Student], tests: List[Test]) -> List[Attempt]:
    return [
        Attempt(
            student_id=random.choice(students).id,
            test_id=random.choice(tests).id
        )
        for _ in range(num_records)
    ]


def generate_open_question_seeder(num_records: int, tests: List[Test]) -> List[OpenQuestion]:
    return [
        OpenQuestion(
            test_id=random.choice(tests).id
        )
        for _ in range(num_records)
    ]


def generate_closed_question_seeder(num_records: int, tests: List[Test]) -> List[ClosedQuestion]:
    return [
        ClosedQuestion(
            test_id=random.choice(tests).id
        )
        for _ in range(num_records)
    ]


def generate_choice_seeder(num_records: int, closed_questions: List[ClosedQuestion]) -> List[Choice]:
    return [
        Choice(
            closed_question_id=random.choice(closed_questions).id
        )
        for _ in range(num_records)
    ]


def generate_closed_answer_seeder(num_records: int, attempts: List[Attempt], closed_questions: List[ClosedQuestion]) -> List[ClosedAnswer]:
    return [
        ClosedAnswer(
            attempt_id=random.choice(attempts).id,
            closed_question_id=random.choice(closed_questions).id
        )
        for _ in range(num_records)
    ]


def generate_closed_answer_choice_seeder(num_records: int, closed_answers: List[ClosedAnswer], choices: List[Choice]) -> List[ClosedAnswerChoice]:
    return [
        ClosedAnswerChoice(
            closed_answer_id=random.choice(closed_answers).id,
            choice_id=random.choice(choices).id
        )
        for _ in range(num_records)
    ]