from data_generating.seeders import *
from data_generating.utils import generate_insert_query
from data_generating.factories.models import Degree
from data_generating.seeders.models_seeder import *

# TERMS = 7
AVG_GROUPS_NUMBER_PER_COURSE = 7
AVG_COURSES_PER_STUDENT = 30
STUDENTS_NUMBER = 1500
# AVG_STUDENT_LIFETIME = 6  # srednia liczba semestrow, na ktorej byl kazdzy student
AVG_GROUP_SIZE = 10
AVG_ENTRIES_PER_GROUP = 5
AVG_OPEN_QUESTIONS_PER_TEST = 2
AVG_CLOSED_QUESTIONS_PER_TEST = 8
AVG_CHOICES_PER_QUESTION = 3
PERC_OF_PEOPLE_UPLOADING_EX = 0.2
PERC_OF_PEOPLE_UPLOADING_TEST = 0.4

# admins_number = 50
faculties_number = 15
admins_faculties_number = 60
fields_of_study_number = 3 * faculties_number                                                   #45
terms_number = fields_of_study_number * 7                                                       #205
courses_number = terms_number * 5                                                               #1_025
college_terms_number = terms_number                                                             #205
# hosts_number = 180
users_number = 3_000
groups_number = courses_number * AVG_GROUPS_NUMBER_PER_COURSE                                   #7_175
students_groups_number = STUDENTS_NUMBER * AVG_COURSES_PER_STUDENT                              #10_500
host_groups_number = int(groups_number * 1.2)                                                   #8_610
hosts_courses_number = int(groups_number * 1.5)                                                 #10_762
entries_number = groups_number * AVG_ENTRIES_PER_GROUP                                          #50_225
comments_of_entries_number = int(entries_number * 0.2)                                          #10_045
entries_files_number = int(entries_number * 0.1)                                                #5_022
exercises_number = int(entries_number * 0.4)                                                    #20_090
solutions_number = int(exercises_number * AVG_GROUP_SIZE * PERC_OF_PEOPLE_UPLOADING_EX)         #40_180
tests_number = courses_number                                                                   #1_025
attempts_number = int(tests_number * AVG_GROUP_SIZE * PERC_OF_PEOPLE_UPLOADING_TEST)            #4_100
open_q_number = tests_number * AVG_OPEN_QUESTIONS_PER_TEST                                      #2_050
open_a_number = int(open_q_number * AVG_GROUP_SIZE * PERC_OF_PEOPLE_UPLOADING_TEST)             #8_200
closed_q_number = tests_number * AVG_CLOSED_QUESTIONS_PER_TEST                                  #8_200
choices_number = closed_q_number * AVG_CHOICES_PER_QUESTION                                     #24_600
closed_answers_number = int(closed_q_number * AVG_GROUP_SIZE * PERC_OF_PEOPLE_UPLOADING_TEST)   #32_800



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

def get_host_group_seeder(
    num_records: int,
    hosts: Sequence[User],
    groups: Sequence[Group],
    host_courses: Sequence[HostCourse],
) -> Sequence[HostGroup]:
    # Mapa host_id -> lista course_id, które host może hostować
    host_to_courses = {}
    for host_course in host_courses:
        if host_course.host_id not in host_to_courses:
            host_to_courses[host_course.host_id] = []
        host_to_courses[host_course.host_id].append(host_course.course_id)

    # Grupy pogrupowane według course_id
    course_to_groups = {}
    for group in groups:
        if group.course_id not in course_to_groups:
            course_to_groups[group.course_id] = []
        course_to_groups[group.course_id].append(group)

    # Gwarancja: Każdy host hostuje przynajmniej jedną grupę dla każdego kursu, który może hostować
    host_groups = set()  # Zmieniamy na set, żeby zapewnić unikalność kombinacji (host_id, group_id)
    for host_id, course_ids in host_to_courses.items():
        for course_id in course_ids:
            if course_id in course_to_groups:
                # Wybierz losową grupę powiązaną z tym kursem
                group = random.choice(course_to_groups[course_id])
                # Dodaj tylko unikalne pary host_id, group_id
                host_groups.add((host_id, group.id))

    # Generowanie dodatkowych losowych wpisów, aby osiągnąć `num_records`
    def random_host_group():
        host = random.choice(hosts)
        group = random.choice(groups)
        return (host.id, group.id)

    # Generowanie unikalnych dodatkowych wpisów
    while len(host_groups) < num_records:
        new_host_group = random_host_group()
        host_groups.add(new_host_group)

    # Tworzenie obiektów HostGroup z unikalnych par host_id, group_id
    host_groups_list = [HostGroup(host_id=host_id, group_id=group_id) for host_id, group_id in host_groups]

    return host_groups_list




degrees = [
    Degree(name="mgr"),
    Degree(name="dr"),
    Degree(name="prof")
]

multiplier = 20
users = generate_users_seeder(users_number * multiplier, list(degrees))
print('users generated')
administrators = list(filter(lambda x: x.profile_type == 0, users))
print('admins generated')
hosts = list(filter(lambda x: x.profile_type == 1, users))
print('hosts generated')
students = list(filter(lambda x: x.profile_type == 2, users))
print('students generated')

students_and_hosts = students + hosts
print('students and hosts generated')

# # # administrators = generate_administrator_seeder(admins_number * multiplier)

faculties = generate_faculty_seeder(faculties_number * multiplier)
print('faculties generated')
faculty_administrators = generate_faculty_administrator_seeder(
    admins_faculties_number * multiplier, faculties, administrators
)
print('faculty admins generated')
fields_of_study = generate_field_of_study_seeder(fields_of_study_number * multiplier, faculties, administrators) #nulls * [None] removed
print('fields of study generated')
terms = generate_term_seeder(terms_number * multiplier, fields_of_study, administrators)
print('terms generated')
courses = generate_course_seeder(courses_number * multiplier, terms, administrators) #nulls * [None] removed
print('courses generated')


college_terms = get_college_terms(college_terms_number * multiplier)
print('college terms generated')

# # # hosts = generate_host_seeder(hosts_number * multiplier, degrees)
groups = generate_group_seeder(groups_number * multiplier, courses, college_terms, hosts) #nulls * [None] removed
print('groups generated')
# # # students = generate_student_seeder(students_number * multiplier)

# # commenters = list(map(lambda x: (x, 3), students)) + list(map(lambda x: (x, 2), hosts))

student_groups = generate_student_group_seeder(
    students_groups_number * multiplier, groups, students, hosts
)
print('student groups generated')
host_courses = generate_host_course_seeder(hosts_courses_number * multiplier, hosts, courses, hosts)
print('host courses generated')
host_groups = get_host_group_seeder(host_groups_number * multiplier, hosts, groups, host_courses)
print('host groups generated')
entries = generate_entry_seeder(entries_number * multiplier, groups, hosts)
print('entries generated')
comment_of_entries = generate_comment_of_entry_seeder(comments_of_entries_number * multiplier, students_and_hosts, entries)
print('comments of entries generated')
entry_files = generate_entry_file_seeder(entries_files_number * multiplier, entries)
print('entry files generated')
exercises = generate_exercise_seeder(exercises_number * multiplier, entries)
print('exercises generated')
solutions = generate_solution_seeder(solutions_number * multiplier, exercises, students)
print('solutions generated')
solution_files = generate_solution_file_seeder(solutions_number * multiplier, solutions)
print('solution files generated')
solution_comments = generate_solution_comment_seeder(solutions_number * multiplier, students_and_hosts, solutions)
print('solution comments generated')
tests = generate_test_seeder(tests_number * multiplier, entries)
print('tests generated')
attempts = generate_attempt_seeder(attempts_number * multiplier, students, tests)
print('attempts generated')
open_questions = generate_open_question_seeder(open_q_number * multiplier, tests)
print('open questions generated')
open_answers = generate_open_answer_seeder(open_a_number * multiplier,attempts, open_questions)
print('open answers generated')
closed_questions = generate_closed_question_seeder(closed_q_number * multiplier, tests)
print('closed questions generated')
# print([type(x) for x in closed_questions])
choices = generate_choice_seeder(choices_number * multiplier, closed_questions)
print('choices generated')
closed_answers = generate_closed_answer_seeder(closed_answers_number * multiplier, attempts, closed_questions)
print('closed answers generated')
closed_answer_choices = generate_closed_answer_choice_seeder(
    closed_answers_number * multiplier, closed_answers, choices
)
print('closed answer choices generated')
# TODO COLLEGE TERMS ARE ALzMOST EMPTY (CHYBA DONE)
# DONE FIELDS OF STUDY DODANE DESCRIPTION (WCZEŚNIEJ "")
# TODO DO NOT FILL FILES TABLE
# TODO DO NOT FILL QUESTIONS TABLE
# TODO ADD OPEN ANSWERS 


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
    open_answers,
    closed_questions,
    choices,
    closed_answers,
    closed_answer_choices,
]

print('created')


with open(f'output_v2_{multiplier}x.txt', 'w') as file:
    for i, table in enumerate(tables):
        print("Table", i, " out of ", len(tables))
        quries_quantity = 0
        query = None
        for j, instance in enumerate(table):
            query = generate_insert_query(instance, query)
            if j % 1000 == 0:
                print("Instance", j, " out of ", len(table))
            quries_quantity += 1
            if quries_quantity == 1000:
                file.writelines(str(query) + ";\n")
                query = None
                quries_quantity = 0
        if query:
            file.writelines(str(query) + ";\n")
            query = None
            quries_quantity = 0

        


