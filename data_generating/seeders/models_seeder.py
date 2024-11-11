from typing import List

from data_generating.factories.models import *
from data_generating.factories.models import Course


def generate_administrator_seeder(num_records: int) -> List[Administrator]:
    return [Administrator() for _ in range(num_records)]


def generate_faculty_seeder(num_records: int) -> List[Faculty]:
    return [Faculty() for _ in range(num_records)]


def generate_faculty_administrator_seeder(num_records: int, faculty_ids: List[str], administrator_ids: List[str]) -> \
        List[FacultyAdministrator]:
    return [
        FacultyAdministrator(
            faculty_id=random.choice(faculty_ids),
            administrator_id=random.choice(administrator_ids)
        )
        for _ in range(num_records)
    ]


def generate_field_of_study_seeder(num_records: int, faculty_ids: List[str], creator_ids: List[str | None]) -> List[
    FieldOfStudy]:
    return [
        FieldOfStudy(
            faculty_id=random.choice(faculty_ids),
            created_by=random.choice(creator_ids),
        )
        for _ in range(num_records)
    ]


def generate_college_term_seeder(num_records: int) -> List[CollegeTerm]:
    return [CollegeTerm() for _ in range(num_records)]


def generate_degree_seeder(num_records: int) -> List[Degree]:
    return [Degree() for _ in range(num_records)]


def generate_host_seeder(num_records: int, degrees: List[str | None]) -> List[Host]:
    return [
        Host(degree=random.choice(degrees))
        for _ in range(num_records)
    ]


def generate_group_seeder(num_records: int, course_ids: List[str], college_term_ids: List[str],
                          creator_ids: List[str | None]) -> List[Group]:
    return [
        Group(
            course_id=random.choice(course_ids),
            college_term_id=random.choice(college_term_ids),
            created_by=random.choice(creator_ids)
        )
        for _ in range(num_records)
    ]


def generate_student_seeder(num_records: int) -> List[Student]:
    return [Student() for _ in range(num_records)]


def generate_student_group_seeder(num_records: int, group_ids: List[str], student_ids: List[str], creator_ids: List[str]) -> List[StudentGroup]:
    return [
        StudentGroup(
            group_id=random.choice(group_ids),
            student_id=random.choice(student_ids),
            created_by=random.choice(creator_ids)
        )
        for _ in range(num_records)
    ]


def generate_host_course_seeder(num_records: int, host_ids: List[str], course_ids: List[str], creator_ids: List[str | None]) -> List[HostCourse]:
    return [
        HostCourse(
            host_id=random.choice(host_ids),
            course_id=random.choice(course_ids),
            created_by=random.choice(creator_ids)
        )
        for _ in range(num_records)
    ]


def generate_entry_seeder(num_records: int, group_ids: List[str | None], host_ids: List[str | None]) -> List[Entry]:
    return [
        Entry(
            group_id=random.choice(group_ids),
            host_id=random.choice(host_ids)
        )
        for _ in range(num_records)
    ]


def generate_comment_of_entry_seeder(num_records: int, commenter_ids: List[str], entry_ids: List[str], commenter_types: List[str]) -> List[CommentOfEntry]:
    return [
        CommentOfEntry(
            commenter_id=random.choice(commenter_ids),
            commenter_type=random.choice(commenter_types),
            entry_id=random.choice(entry_ids)
        )
        for _ in range(num_records)
    ]


def generate_entry_file_seeder(num_records: int, entry_ids: List[str]) -> List[EntryFile]:
    return [
        EntryFile(
            entry_id=random.choice(entry_ids)
        )
        for _ in range(num_records)
    ]


def generate_exercise_seeder(num_records: int, entry_ids: List[str]) -> List[Exercise]:
    return [
        Exercise(
            entry_id=random.choice(entry_ids)
        )
        for _ in range(num_records)
    ]


def generate_solution_seeder(num_records: int, exercise_ids: List[str], student_ids: List[str]) -> List[Solution]:
    return [
        Solution(
            exercise_id=random.choice(exercise_ids),
            student_id=random.choice(student_ids)
        )
        for _ in range(num_records)
    ]


def generate_solution_file_seeder(num_records: int, solution_ids: List[str]) -> List[SolutionFile]:
    return [
        SolutionFile(
            solution_id=random.choice(solution_ids)
        )
        for _ in range(num_records)
    ]


def generate_solution_comment_seeder(num_records: int, commenter_ids: List[str | None], commenter_types: List[int | None], solution_ids: List[str]) -> List[SolutionComment]:
    return [
        SolutionComment(
            commenter_id=random.choice(commenter_ids),
            commenter_type=random.choice(commenter_types),
            solution_id=random.choice(solution_ids)
        )
        for _ in range(num_records)
    ]


def generate_test_seeder(num_records: int, entry_ids: List[str]) -> List[Test]:
    return [
        Test(
            entry_id=random.choice(entry_ids)
        )
        for _ in range(num_records)
    ]


def generate_attempt_seeder(num_records: int, student_ids: List[str], test_ids: List[str]) -> List[Attempt]:
    return [
        Attempt(
            student_id=random.choice(student_ids),
            test_id=random.choice(test_ids)
        )
        for _ in range(num_records)
    ]


def generate_open_question_seeder(num_records: int, test_ids: List[str]) -> List[OpenQuestion]:
    return [
        OpenQuestion(
            test_id=random.choice(test_ids)
        )
        for _ in range(num_records)
    ]


def generate_closed_question_seeder(num_records: int, test_ids: List[str]) -> List[ClosedQuestion]:
    return [
        ClosedQuestion(
            test_id=random.choice(test_ids)
        )
        for _ in range(num_records)
    ]


def generate_choice_seeder(num_records: int, closed_question_ids: List[str]) -> List[Choice]:
    return [
        Choice(
            closed_question_id=random.choice(closed_question_ids)
        )
        for _ in range(num_records)
    ]


def generate_closed_answer_seeder(num_records: int, attempt_ids: List[str], closed_question_ids: List[str]) -> List[ClosedAnswer]:
    return [
        ClosedAnswer(
            attempt_id=random.choice(attempt_ids),
            closed_question_id=random.choice(closed_question_ids)
        )
        for _ in range(num_records)
    ]


def generate_closed_answer_choice_seeder(num_records: int, closed_answer_ids: List[str], choice_ids: List[str]) -> List[ClosedAnswerChoice]:
    return [
        ClosedAnswerChoice(
            closed_answer_id=random.choice(closed_answer_ids),
            choice_id=random.choice(choice_ids)
        )
        for _ in range(num_records)
    ]

