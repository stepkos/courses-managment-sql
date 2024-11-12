from data_generating.seeders import *
from data_generating.utils import generate_insert_query

num_records = 1_000
nulls = 0

degrees = generate_degree_seeder(num_records)
users = generate_users_seeder(3 * num_records, list(degrees))
administrators = list(filter(lambda x: x.profile_type == 0, users))
hosts = list(filter(lambda x: x.profile_type == 1, users))
students = list(filter(lambda x: x.profile_type == 2, users))
student_and_hosts = students + hosts

faculties = generate_faculty_seeder(num_records)
faculty_administrators = generate_faculty_administrator_seeder(
    num_records, faculties, administrators
)
fields_of_study = generate_field_of_study_seeder(num_records, faculties, administrators + nulls * [None])
terms = generate_term_seeder(num_records, fields_of_study, administrators)
courses = generate_course_seeder(num_records, terms, administrators + nulls * [None])
college_terms = generate_college_term_seeder(num_records)
groups = generate_group_seeder(num_records, courses, college_terms, hosts + nulls * [None])
student_groups = generate_student_group_seeder(
    num_records, groups, students, hosts 
)
host_groups = generate_host_group_seeder(num_records, hosts, groups)
host_courses = generate_host_course_seeder(num_records, hosts, courses, hosts + nulls * [None])
entries = generate_entry_seeder(num_records, groups + nulls * [None], hosts + nulls * [None])
comment_of_entries = generate_comment_of_entry_seeder(num_records, student_and_hosts, entries)
entry_files = generate_entry_file_seeder(num_records, entries)
exercises = generate_exercise_seeder(num_records, entries)
solutions = generate_solution_seeder(num_records, exercises, students)
solution_files = generate_solution_file_seeder(num_records, solutions)
solution_comments = generate_solution_comment_seeder(num_records, student_and_hosts + nulls * [None], solutions)
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
    degrees,
    administrators,
    faculties,
    faculty_administrators,
    fields_of_study,
    terms,
    courses,
    college_terms,
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