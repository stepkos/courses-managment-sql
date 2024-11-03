DROP TABLE IF EXISTS public.open_answers;
DROP TABLE IF EXISTS public.closed_answer_choices;
DROP TABLE IF EXISTS public.closed_answers;
DROP TABLE IF EXISTS public.choices;
DROP TABLE IF EXISTS public.closed_questions;
DROP TABLE IF EXISTS public.open_questions;
DROP TABLE IF EXISTS public.attempts;
DROP TABLE IF EXISTS public.tests;
DROP TABLE IF EXISTS public.solution_comments;
DROP TABLE IF EXISTS public.solution_files;
DROP TABLE IF EXISTS public.solutions;
DROP TABLE IF EXISTS public.exercises;
DROP TABLE IF EXISTS public.entry_files;
DROP TABLE IF EXISTS public.comment_entries;
DROP TABLE IF EXISTS public.entries;
DROP TABLE IF EXISTS public.host_courses;
DROP TABLE IF EXISTS public.host_groups;
DROP TABLE IF EXISTS public.student_groups;
DROP TABLE IF EXISTS public.students;
DROP TABLE IF EXISTS public.groups;
DROP TABLE IF EXISTS public.hosts;
DROP TABLE IF EXISTS public.college_terms;
DROP TABLE IF EXISTS public.courses;
DROP TABLE IF EXISTS public.terms;
DROP TABLE IF EXISTS public.fields_of_study;
DROP TABLE IF EXISTS public.faculty_administrators;
DROP TABLE IF EXISTS public.faculties;
DROP TABLE IF EXISTS public.administrators;

CREATE TABLE IF NOT EXISTS public.administrators (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    is_active BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS public.faculties (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    website VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS public.faculty_administrators (
    id SERIAL PRIMARY KEY,
    faculty_id INTEGER REFERENCES faculties(id),
    administrator_id INTEGER REFERENCES administrators(id)
);

CREATE TABLE IF NOT EXISTS public.fields_of_study (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    faculty_id INTEGER REFERENCES faculties(id),
    description TEXT,
    start_year INTEGER
);

CREATE TABLE IF NOT EXISTS public.terms (
    id SERIAL PRIMARY KEY,
    field_of_study_id INTEGER REFERENCES fields_of_study(id),
    order_number INTEGER
);

CREATE TABLE IF NOT EXISTS public.courses (
    id SERIAL PRIMARY KEY,
    term_id INTEGER REFERENCES terms(id),
    title VARCHAR(255),
    description TEXT
);

CREATE TABLE IF NOT EXISTS public.college_terms (
    id SERIAL PRIMARY KEY,
    start_date TIMESTAMP,
    end_date TIMESTAMP
);

CREATE TABLE IF NOT EXISTS public.hosts (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    surname VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255),
    is_active BOOLEAN,
    degree VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS public.groups (
    id SERIAL PRIMARY KEY,
    course_id INTEGER REFERENCES courses(id),
    college_term_id INTEGER REFERENCES college_terms(id),
    host_id INTEGER REFERENCES hosts(id),
    name VARCHAR(255),
    description TEXT,
    image VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS public.students (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    surname VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255),
    is_active BOOLEAN
);

CREATE TABLE IF NOT EXISTS public.student_groups (
    id SERIAL PRIMARY KEY,
    group_id INTEGER REFERENCES groups(id),
    student_id INTEGER REFERENCES students(id)
);

CREATE TABLE IF NOT EXISTS public.host_groups (
    id SERIAL PRIMARY KEY,
    host_id INTEGER REFERENCES hosts(id),
    group_id INTEGER REFERENCES groups(id)
);

CREATE TABLE IF NOT EXISTS public.host_courses (
    id SERIAL PRIMARY KEY,
    host_id INTEGER REFERENCES hosts(id),
    course_id INTEGER REFERENCES courses(id),
    is_course_admin BOOLEAN
);

CREATE TABLE IF NOT EXISTS public.entries (
    id SERIAL PRIMARY KEY,
    group_id INTEGER REFERENCES groups(id),
    title VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    content TEXT,
    host_id INTEGER REFERENCES hosts(id)
);

CREATE TABLE IF NOT EXISTS public.comment_entries (
    id SERIAL PRIMARY KEY,
    commenter_id INTEGER,
    commenter_type VARCHAR(255),
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    entry_id INTEGER REFERENCES entries(id)
);

CREATE TABLE IF NOT EXISTS public.entry_files (
    id SERIAL PRIMARY KEY,
    file_url VARCHAR(255),
    uploaded_at TIMESTAMP,
    entry_id INTEGER REFERENCES entries(id)
);

CREATE TABLE IF NOT EXISTS public.exercises (
    id SERIAL PRIMARY KEY,
    entry_id INTEGER REFERENCES entries(id),
    due_date TIMESTAMP
);

CREATE TABLE IF NOT EXISTS public.solutions (
    id SERIAL PRIMARY KEY,
    exercise_id INTEGER REFERENCES exercises(id),
    student_id INTEGER REFERENCES students(id),
    grade INTEGER,
    submitted_at TIMESTAMP,
    text_answer TEXT
);

CREATE TABLE IF NOT EXISTS public.solution_files (
    id SERIAL PRIMARY KEY,
    file_url VARCHAR(255),
    uploaded_at TIMESTAMP,
    solution_id INTEGER REFERENCES solutions(id)
);

CREATE TABLE IF NOT EXISTS public.solution_comments (
    id SERIAL PRIMARY KEY,
    commenter_id INTEGER,
    commenter_type VARCHAR(255),
    solution_id INTEGER REFERENCES solutions(id),
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS public.tests (
    id SERIAL PRIMARY KEY,
    entry_id INTEGER REFERENCES entries(id),
    title VARCHAR(255),
    description TEXT,
    available_from_date TIMESTAMP,
    available_to_date TIMESTAMP,
    max_seconds_for_open INTEGER,
    max_seconds_for_closed INTEGER,
    duration_in_minutes INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS public.attempts (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES students(id),
    test_id INTEGER REFERENCES tests(id),
    score INTEGER,
    attempt_at TIMESTAMP,
    submitted_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS public.open_questions (
    id SERIAL PRIMARY KEY,
    test_id INTEGER REFERENCES tests(id),
    content TEXT,
    points INTEGER
);

CREATE TABLE IF NOT EXISTS public.closed_questions (
    id SERIAL PRIMARY KEY,
    test_id INTEGER REFERENCES tests(id),
    content TEXT,
    points INTEGER,
    type VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS public.choices (
    id SERIAL PRIMARY KEY,
    closed_question_id INTEGER REFERENCES closed_questions(id),
    content TEXT,
    is_correct BOOLEAN
);

CREATE TABLE IF NOT EXISTS public.closed_answers (
    id SERIAL PRIMARY KEY,
    is_correct BOOLEAN,
    submitted_at TIMESTAMP,
    closed_question_id INTEGER REFERENCES closed_questions(id),
    attempt_id INTEGER REFERENCES attempts(id)
);

CREATE TABLE IF NOT EXISTS public.closed_answer_choices (
    id SERIAL PRIMARY KEY,
    closed_answer_id INTEGER REFERENCES closed_answers(id),
    choice_id INTEGER REFERENCES choices(id)
);

CREATE TABLE IF NOT EXISTS public.open_answers (
    id SERIAL PRIMARY KEY,
    is_correct BOOLEAN,
    submitted_at TIMESTAMP,
    open_question_id INTEGER REFERENCES open_questions(id),
    content TEXT,
    attempt_id INTEGER REFERENCES attempts(id)
);
