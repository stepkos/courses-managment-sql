from data_generating.seeders import *
from data_generating.utils import generate_insert_query

TERMS = 7
AVG_GROUP_SIZE = 20
AVG_STUDENT_LIFETIME = 6 #srednia liczba semestrow, na ktorej byl kazdzy student
AVG_GROUPS_NUMBER_PER_COURSE = 7
AVG_ENTRIES_PER_GROUP = 12

admins_number = 50
faculties_number = 15
admins_faculties_number = 90
fields_of_study_number = 80
terms_number = fields_of_study_number * 20
courses_number = terms_number * 5
college_terms_number = 20
hosts_number = 1_800
students_number = 40_000
groups_number = courses_number * college_terms_number / TERMS * students_number / AVG_GROUP_SIZE / faculties_number
students_groups_number = students_number * AVG_STUDENT_LIFETIME
host_groups_number = int(groups_number * 1.2)
hosts_courses_number = courses_number * AVG_GROUPS_NUMBER_PER_COURSE
entries_number = courses_number * AVG_ENTRIES_PER_GROUP
comments_of_entries_number = entries_number * 0.3
entries_files_number = entries_number * 0.1
exercises_number = entries_number * 0.95
solutions_number = exercises_number * college_terms_number * AVG_GROUP_SIZE



def get_college_terms(n: int) -> List[CollegeTerm]:
    terms = []
    base_year = fake.date_this_century().year  # losowy rok początkowy, np. 2020

    for i in range(n):
        if i % 2 == 0:  # Semestr zimowy (parzyste indeksy)
            start_date = f"{base_year + i // 2}-10-01"
            end_date = f"{base_year + i // 2 + 1}-02-15"
        else:  # Semestr letni (nieparzyste indeksy)
            start_date = f"{base_year + i // 2 + 1}-02-16"
            end_date = f"{base_year + i // 2 + 1}-06-30"

        term = CollegeTerm(start_date=start_date, end_date=end_date)
        terms.append(term)
        return terms



administrators = generate_administrator_seeder(admins_number)
faculties = generate_faculty_seeder(faculties_number)
faculty_administrators = generate_faculty_administrator_seeder(
    admins_faculties_number, faculties, administrators
)
fields_of_study = generate_field_of_study_seeder(num_records, faculties, administrators)
terms = generate_term_seeder(num_records, fields_of_study, administrators)
courses = generate_course_seeder(num_records, terms, administrators)
college_terms = generate_college_term_seeder(num_records)
groups = generate_group_seeder(num_records, courses, college_terms, hosts)
student_groups = generate_student_group_seeder(num_records, groups, students, hosts)
host_groups = generate_host_group_seeder(num_records, hosts, groups)
host_courses = generate_host_course_seeder(num_records, hosts, courses, hosts)
entries = generate_entry_seeder(num_records, groups, hosts)
comment_of_entries = generate_comment_of_entry_seeder(
    num_records, student_and_hosts, entries
)
entry_files = generate_entry_file_seeder(num_records, entries)
exercises = generate_exercise_seeder(num_records, entries)
solutions = generate_solution_seeder(num_records, exercises, students)
solution_files = generate_solution_file_seeder(num_records, solutions)
solution_comments = generate_solution_comment_seeder(
    num_records, student_and_hosts, solutions
)
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
# 2 nulle
# num_records randomowe
