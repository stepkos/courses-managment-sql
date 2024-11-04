-- DROPS

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

-- ABSTRACT TABLES

CREATE TABLE IF NOT EXISTS public.users (
    first_name VARCHAR(50) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    email TEXT CHECK (email ~* '^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$') UNIQUE,
    password TEXT NOT NULL,
    is_active BOOLEAN
);

CREATE TABLE IF NOT EXISTS public.answers (
    points INTEGER,
    submitted_at TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS public.question (
    content TEXT,
    points INTEGER
);

CREATE TABLE IF NOT EXISTS public.files (
    file_url TEXT CHECK (file_url ~* '^(https?:\/\/)?([\da-z.-]+)\.([a-z.]{2,6})([/\w .-]*)*\/?$'),
    uploaded_at TIMESTAMPTZ
);

-- CONCRETE TABLES

CREATE TABLE IF NOT EXISTS public.administrators (
	id SERIAL PRIMARY KEY
) INHERITS (public.users);

CREATE TABLE IF NOT EXISTS public.faculties (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) CHECK (email ~* '^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'),
    phone VARCHAR(20) CHECK (phone ~* '^\+?[0-9\s-]*$'),
    website VARCHAR(2048) CHECK (website ~* '^(https?:\/\/)?([\da-z.-]+)\.([a-z.]{2,6})([/\w .-]*)*\/?$')
);

CREATE TABLE IF NOT EXISTS public.faculty_administrators (
    id SERIAL PRIMARY KEY,
    faculty_id INTEGER REFERENCES faculties(id) NOT NULL,
    administrator_id INTEGER REFERENCES administrators(id) NOT NULL
);

CREATE TABLE IF NOT EXISTS public.fields_of_study (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    faculty_id INTEGER REFERENCES faculties(id) NOT NULL,
    description VARCHAR(255) NOT NULL,
    start_year INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS public.terms (
    id SERIAL PRIMARY KEY,
    field_of_study_id INTEGER REFERENCES fields_of_study(id) NOT NULL,
    order_number INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS public.courses (
    id SERIAL PRIMARY KEY,
    term_id INTEGER REFERENCES terms(id) NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS public.college_terms (
    id SERIAL PRIMARY KEY,
    start_date TIMESTAMPTZ NOT NULL,
    end_date TIMESTAMPTZ NOT NULL
);

CREATE TABLE IF NOT EXISTS public.hosts (
    id SERIAL PRIMARY KEY,
    degree VARCHAR(255)
) INHERITS (public.users);

CREATE TABLE IF NOT EXISTS public.groups (
    id SERIAL PRIMARY KEY,
    course_id INTEGER REFERENCES courses(id) NOT NULL,
    college_term_id INTEGER REFERENCES college_terms(id) NOT NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    image TEXT CHECK (image ~* '^(https?:\/\/)?([\da-z.-]+)\.([a-z.]{2,6})([/\w .-]*)*\/?$')
);

CREATE TABLE IF NOT EXISTS public.students (
	id SERIAL PRIMARY KEY
) INHERITS (public.users);

CREATE TABLE IF NOT EXISTS public.student_groups (
    id SERIAL PRIMARY KEY,
    group_id INTEGER REFERENCES groups(id) NOT NULL,
    student_id INTEGER REFERENCES students(id) NOT NULL
);

CREATE TABLE IF NOT EXISTS public.host_groups (
    id SERIAL PRIMARY KEY,
    host_id INTEGER REFERENCES hosts(id) NOT NULL,
    group_id INTEGER REFERENCES groups(id) NOT NULL
);

CREATE TABLE IF NOT EXISTS public.host_courses (
    id SERIAL PRIMARY KEY,
    host_id INTEGER REFERENCES hosts(id) NOT NULL,
    course_id INTEGER REFERENCES courses(id) NOT NULL,
    is_course_admin BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS public.entries (
    id SERIAL PRIMARY KEY,
    group_id INTEGER REFERENCES groups(id) NOT NULL,
    title VARCHAR(255) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    content TEXT NOT NULL,
    host_id INTEGER REFERENCES hosts(id) NOT NULL
);

CREATE TABLE IF NOT EXISTS public.comment_entries (
    id SERIAL PRIMARY KEY,
    commenter_id INTEGER,
    commenter_type VARCHAR(255),
    content TEXT,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    entry_id INTEGER REFERENCES entries(id)
);

CREATE TABLE IF NOT EXISTS public.entry_files (
    id SERIAL PRIMARY KEY,
    entry_id INTEGER REFERENCES entries(id)
) INHERITS (public.files);

CREATE TABLE IF NOT EXISTS public.exercises (
    id SERIAL PRIMARY KEY,
    entry_id INTEGER REFERENCES entries(id),
    due_date TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS public.solutions (
    id SERIAL PRIMARY KEY,
    exercise_id INTEGER REFERENCES exercises(id),
    student_id INTEGER REFERENCES students(id),
    grade INTEGER,
    submitted_at TIMESTAMPTZ,
    text_answer TEXT
);

CREATE TABLE IF NOT EXISTS public.solution_files (
    id SERIAL PRIMARY KEY,
    solution_id INTEGER REFERENCES solutions(id)
) INHERITS (public.files);

CREATE TABLE IF NOT EXISTS public.solution_comments (
    id SERIAL PRIMARY KEY,
    commenter_id INTEGER,
    commenter_type VARCHAR(255),
    solution_id INTEGER REFERENCES solutions(id),
    content TEXT,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS public.tests (
    id SERIAL PRIMARY KEY,
    entry_id INTEGER REFERENCES entries(id),
    title VARCHAR(255),
    description TEXT,
    available_from_date TIMESTAMPTZ,
    available_to_date TIMESTAMPTZ,
    max_seconds_for_open INTEGER,
    max_seconds_for_closed INTEGER,
    duration_in_minutes INTEGER,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS public.attempts (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES students(id),
    test_id INTEGER REFERENCES tests(id),
    score INTEGER,
    attempt_at TIMESTAMPTZ,
    submitted_at TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS public.open_questions (
    id SERIAL PRIMARY KEY,
    test_id INTEGER REFERENCES tests(id),
) INHERITS (public.question);

CREATE TABLE IF NOT EXISTS public.closed_questions (
    id SERIAL PRIMARY KEY,
    test_id INTEGER REFERENCES tests(id),
    type VARCHAR(255)
) INHERITS (public.question);

CREATE TABLE IF NOT EXISTS public.choices (
    id SERIAL PRIMARY KEY,
    closed_question_id INTEGER REFERENCES closed_questions(id),
    content TEXT,
    is_correct BOOLEAN
);

CREATE TABLE IF NOT EXISTS public.closed_answers (
    id SERIAL PRIMARY KEY,
    submitted_at TIMESTAMPTZ,
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
    submitted_at TIMESTAMPTZ,
    open_question_id INTEGER REFERENCES open_questions(id),
    content TEXT,
    attempt_id INTEGER REFERENCES attempts(id)
);
