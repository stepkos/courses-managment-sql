from data_generating.seeders.models_seeder import *
from data_generating.utils import generate_insert_query

num_records = 1_000

administrators = generate_administrator_seeder(num_records)
faculties = generate_faculty_seeder(num_records)
faculty_administrators = generate_faculty_administrator_seeder(
    num_records, faculties, administrators
)
fields_of_study = generate_field_of_study_seeder(num_records, faculties, administrators)
terms = generate_term_seeder(num_records, fields_of_study, administrators)
courses = generate_course_seeder(num_records, terms, administrators)
college_terms = generate_college_term_seeder(num_records)
degrees = generate_degree_seeder(num_records)
hosts = generate_host_seeder(num_records, degrees)
groups = generate_group_seeder(num_records, courses, college_terms, hosts)
students = generate_student_seeder(num_records)

commenters = list(map(lambda x: (x, 3), students)) + list(map(lambda x: (x, 2), hosts))

student_groups = generate_student_group_seeder(
    num_records, groups, students, hosts 
)
host_groups = generate_host_group_seeder(num_records, hosts, groups)
host_courses = generate_host_course_seeder(num_records, hosts, courses, hosts)
entries = generate_entry_seeder(num_records, groups, hosts)
comment_of_entries = generate_comment_of_entry_seeder(num_records, commenters, entries)
entry_files = generate_entry_file_seeder(num_records, entries)
exercises = generate_exercise_seeder(num_records, entries)
solutions = generate_solution_seeder(num_records, exercises, students)
solution_files = generate_solution_file_seeder(num_records, solutions)
solution_comments = generate_solution_comment_seeder(num_records, commenters, solutions)
tests = generate_test_seeder(num_records, entries)
attempts = generate_attempt_seeder(num_records, students, tests)
open_questions = generate_open_question_seeder(num_records, tests)
closed_questions = generate_closed_question_seeder(num_records, tests)
choices = generate_choice_seeder(num_records, closed_questions)
closed_answers = generate_closed_answer_seeder(num_records, attempts, closed_questions)
closed_answer_choices = generate_closed_answer_choice_seeder(
    num_records, closed_answers, choices
)


tables: list[Sequence[BaseModel]] = [
    administrators,
    faculties,
    faculty_administrators,
    fields_of_study,
    terms,
    courses,
    college_terms,
    degrees,
    hosts,
    groups,
    students,
    student_groups,
    host_groups,
    host_courses,
    entries,
    comment_of_entries,
    entry_files,
    exercises,
    solutions,
    solution_files,
    solution_comments,
    tests,
    attempts,
    open_questions,
    closed_questions,
    choices,
    closed_answers,
    closed_answer_choices,
]

print("".join(map(lambda x: generate_insert_query(x) + ";\n", tables)))


# 1 czy robimy user profile, imo tak
# 2 uniqueness
