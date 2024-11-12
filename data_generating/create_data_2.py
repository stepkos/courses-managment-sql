from data_generating.seeders import *
from data_generating.utils import generate_insert_query

TERMS = 7
AVG_GROUP_SIZE = 20
AVG_STUDENT_LIFETIME = 6  # srednia liczba semestrow, na ktorej byl kazdzy student
AVG_GROUPS_NUMBER_PER_COURSE = 7
AVG_ENTRIES_PER_GROUP = 12
AVG_OPEN_QUESTIONS_PER_TEST = 4
AVG_CLOSED_QUESTIONS_PER_TEST = 16
AVG_CHOICES_PER_QUESTION = 4

admins_number = 50
faculties_number = 15
admins_faculties_number = 90
fields_of_study_number = 30
terms_number = fields_of_study_number * 5
courses_number = terms_number * 5
college_terms_number = 10
hosts_number = 180
students_number = 4_000
groups_number = int(courses_number * college_terms_number / TERMS * students_number / AVG_GROUP_SIZE / faculties_number)
students_groups_number = int(students_number * AVG_STUDENT_LIFETIME)
host_groups_number = int(groups_number * 1.2)
hosts_courses_number = int(courses_number * AVG_GROUPS_NUMBER_PER_COURSE)
entries_number = int(courses_number * AVG_ENTRIES_PER_GROUP)
comments_of_entries_number = int(entries_number * 0.3)
entries_files_number = int(entries_number * 0.1)
exercises_number = int(entries_number * 0.45)
solutions_number = int(exercises_number * college_terms_number * AVG_GROUP_SIZE)


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


degrees = [
    Degree(name="mgr"),
    Degree(name="dr"),
    Degree(name="prof")
]

users = generate_users_seeder(students_number * 2, list(degrees))
administrators = list(filter(lambda x: x.profile_type == 0, users))
hosts = list(filter(lambda x: x.profile_type == 1, users))
students = list(filter(lambda x: x.profile_type == 2, users))

# administrators = generate_administrator_seeder(admins_number)

faculties = generate_faculty_seeder(faculties_number)
faculty_administrators = generate_faculty_administrator_seeder(
    admins_faculties_number, faculties, administrators
)
fields_of_study = generate_field_of_study_seeder(fields_of_study_number, faculties, administrators)
terms = generate_term_seeder(terms_number, fields_of_study, administrators)
courses = generate_course_seeder(courses_number, terms, administrators)


college_terms = get_college_terms(college_terms_number)

# hosts = generate_host_seeder(hosts_number, degrees)
groups = generate_group_seeder(groups_number, courses, college_terms, hosts)
# students = generate_student_seeder(students_number)

commenters = list(map(lambda x: (x, 3), students)) + list(map(lambda x: (x, 2), hosts))

student_groups = generate_student_group_seeder(
    int(students_groups_number), groups, students, hosts
)
host_groups = generate_host_group_seeder(host_groups_number, hosts, groups)
host_courses = generate_host_course_seeder(hosts_courses_number, hosts, courses, hosts)
entries = generate_entry_seeder(entries_number, groups, hosts)
comment_of_entries = generate_comment_of_entry_seeder(comments_of_entries_number, commenters, entries)
entry_files = generate_entry_file_seeder(entries_files_number, entries)
exercises = generate_exercise_seeder(exercises_number, entries)
solutions = generate_solution_seeder(solutions_number, exercises, students)
solution_files = generate_solution_file_seeder(solutions_number, solutions)
solution_comments = generate_solution_comment_seeder(solutions_number, commenters, solutions)
tests = generate_test_seeder(courses_number, entries)
attempts = generate_attempt_seeder(courses_number * AVG_GROUP_SIZE, students, tests)
open_questions = generate_open_question_seeder(AVG_OPEN_QUESTIONS_PER_TEST * courses_number, tests)
closed_questions = generate_closed_question_seeder(AVG_CLOSED_QUESTIONS_PER_TEST * courses_number, tests)
choices = generate_choice_seeder(AVG_CLOSED_QUESTIONS_PER_TEST * courses_number * AVG_CHOICES_PER_QUESTION, closed_questions)
closed_answers = generate_closed_answer_seeder(AVG_CLOSED_QUESTIONS_PER_TEST * courses_number * AVG_GROUP_SIZE, attempts, closed_questions)
closed_answer_choices = generate_closed_answer_choice_seeder(
    AVG_CLOSED_QUESTIONS_PER_TEST * courses_number * AVG_GROUP_SIZE, closed_answers, choices
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



