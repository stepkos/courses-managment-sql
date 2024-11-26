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
DROP TABLE IF EXISTS public.comment_of_entries;
DROP TABLE IF EXISTS public.entries;
DROP TABLE IF EXISTS public.host_courses;
DROP TABLE IF EXISTS public.host_groups;
DROP TABLE IF EXISTS public.student_groups;
DROP TABLE IF EXISTS public.groups;
DROP TABLE IF EXISTS public.college_terms;
DROP TABLE IF EXISTS public.courses;
DROP TABLE IF EXISTS public.terms;
DROP TABLE IF EXISTS public.fields_of_study;
DROP TABLE IF EXISTS public.faculty_administrators;
DROP TABLE IF EXISTS public.faculties;
DROP TABLE IF EXISTS public.users;
DROP TABLE IF EXISTS public.answers;
DROP TABLE IF EXISTS public.questions;
DROP TABLE IF EXISTS public.files;
DROP TABLE IF EXISTS public.degrees;

-- ABSTRACT TABLES

CREATE TABLE IF NOT EXISTS public.answers (
    points INTEGER,
    submitted_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS public.questions (
    content TEXT NOT NULL,
    points INTEGER NOT NULL 
);

CREATE TABLE IF NOT EXISTS public.files (
    file_url TEXT NOT NULL CHECK (file_url ~* '^(https?:\/\/)?([\da-z.-]+)\.([a-z.]{2,6})([/\w .-]*)*\/?$'),
    uploaded_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- CONCRETE TABLES

CREATE TABLE IF NOT EXISTS public.degrees (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS public.users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    first_name VARCHAR(50) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    email TEXT CHECK (email ~* '^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'),
    password TEXT NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    degree UUID REFERENCES degrees(id) ON DELETE SET NULL,
    profile_type INTEGER NOT NULL, -- 0 - administrator, 1 - host, 2 - student
    CONSTRAINT unique_user_email UNIQUE (email)
);

CREATE TABLE IF NOT EXISTS public.faculties (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) CHECK (email ~* '^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'),
    phone VARCHAR(20) CHECK (phone ~* '^(\+\d+ )?[\d\s-]*$'),
    website VARCHAR(2048) CHECK (website ~* '^(https?:\/\/)?([\da-z.-]+)\.([a-z.]{2,6})([/\w .-]*)*\/?$')
);

CREATE TABLE IF NOT EXISTS public.faculty_administrators (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    faculty_id UUID NOT NULL REFERENCES faculties(id) ON DELETE CASCADE,
    administrator_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    CONSTRAINT unique_faculty_administrator UNIQUE (faculty_id, administrator_id)
);

CREATE TABLE IF NOT EXISTS public.fields_of_study (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    faculty_id UUID NOT NULL REFERENCES faculties(id),
    description TEXT NOT NULL DEFAULT '',
    start_year INTEGER NOT NULL,
    created_by UUID REFERENCES users(id) ON DELETE SET NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS public.terms (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    field_of_study_id UUID NOT NULL REFERENCES fields_of_study(id),
    term_number INTEGER NOT NULL,
    created_by UUID REFERENCES users(id) ON DELETE SET NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS public.courses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    term_id UUID NOT NULL REFERENCES terms(id),
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL DEFAULT '',
    created_by UUID REFERENCES users(id),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS public.college_terms (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    start_date TIMESTAMPTZ NOT NULL,
    end_date TIMESTAMPTZ NOT NULL
);

CREATE TABLE IF NOT EXISTS public.groups (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    course_id UUID NOT NULL REFERENCES courses(id),
    college_term_id UUID NOT NULL REFERENCES college_terms(id),
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL DEFAULT '',
    image TEXT CHECK (image ~* '^(https?:\/\/)?([\da-z.-]+)\.([a-z.]{2,6})([/\w .-]*)*\/?$' OR image IS NULL),
    created_by UUID REFERENCES users(id) ON DELETE SET NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS public.student_groups (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    group_id UUID NOT NULL REFERENCES groups(id),
    student_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    created_by UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT unique_student_group UNIQUE (student_id, group_id)
);

CREATE TABLE IF NOT EXISTS public.host_groups (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    host_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    group_id UUID NOT NULL REFERENCES groups(id) ON DELETE CASCADE,
    CONSTRAINT unique_host_group UNIQUE (host_id, group_id)
);

CREATE TABLE IF NOT EXISTS public.host_courses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    host_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    course_id UUID NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
    is_course_admin BOOLEAN NOT NULL,
    created_by UUID NOT NULL REFERENCES users(id),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS public.entries (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    group_id UUID NOT NULL REFERENCES groups(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    content TEXT NOT NULL,
    host_id UUID REFERENCES users(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS public.comment_of_entries (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE SET NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    entry_id UUID NOT NULL REFERENCES entries(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS public.entry_files (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    entry_id UUID NOT NULL REFERENCES entries(id) ON DELETE CASCADE
) INHERITS (public.files);

CREATE TABLE IF NOT EXISTS public.exercises (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    entry_id UUID NOT NULL REFERENCES entries(id) ON DELETE CASCADE,
    due_date TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS public.solutions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    exercise_id UUID NOT NULL REFERENCES exercises(id) ON DELETE CASCADE,
    student_id UUID REFERENCES users(id) ON DELETE SET NULL,
    grade NUMERIC(4, 2) NOT NULL CHECK (grade >= 0.00 AND grade <= 10.00),
    submitted_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    text_answer TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS public.solution_files (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    solution_id UUID NOT NULL REFERENCES solutions(id) ON DELETE CASCADE
) INHERITS (public.files);

CREATE TABLE IF NOT EXISTS public.solution_comments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE SET NULL,
    solution_id UUID NOT NULL REFERENCES solutions(id) ON DELETE CASCADE,
    content TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS public.tests (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    entry_id UUID NOT NULL REFERENCES entries(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL DEFAULT '',
    available_from_date TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    available_to_date TIMESTAMPTZ,
    max_seconds_for_open INTEGER,
    max_seconds_for_closed INTEGER,
    duration_in_minutes INTEGER CHECK (duration_in_minutes >= 0),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS public.attempts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    student_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    test_id UUID NOT NULL REFERENCES tests(id) ON DELETE CASCADE,
    score NUMERIC(5,2) CHECK (score >= 0.00 AND score <= 100.00 OR score IS NULL),
    started_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    submitted_at TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS public.open_questions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    test_id UUID NOT NULL REFERENCES tests(id) ON DELETE CASCADE
) INHERITS (public.questions);

CREATE TABLE IF NOT EXISTS public.closed_questions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    test_id UUID NOT NULL REFERENCES tests(id) ON DELETE CASCADE,
    is_multiple BOOLEAN NOT NULL 
) INHERITS (public.questions);

CREATE TABLE IF NOT EXISTS public.choices (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    closed_question_id UUID NOT NULL REFERENCES closed_questions(id) ON DELETE CASCADE,
    content TEXT NOT NULL,
    is_correct BOOLEAN
);

CREATE TABLE IF NOT EXISTS public.closed_answers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    attempt_id UUID NOT NULL REFERENCES attempts(id) ON DELETE CASCADE,
    closed_question_id UUID NOT NULL REFERENCES closed_questions(id) ON DELETE CASCADE,
    submitted_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
) INHERITS (public.answers);

CREATE TABLE IF NOT EXISTS public.closed_answer_choices (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    closed_answer_id UUID NOT NULL REFERENCES closed_answers(id) ON DELETE CASCADE,
    choice_id UUID NOT NULL REFERENCES choices(id) ON DELETE CASCADE,
    CONSTRAINT unique_closed_answer_choice UNIQUE (closed_answer_id, choice_id)
);

CREATE TABLE IF NOT EXISTS public.open_answers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    open_question_id UUID NOT NULL REFERENCES open_questions(id) ON DELETE CASCADE,
    content TEXT NOT NULL,
    attempt_id UUID NOT NULL REFERENCES attempts(id) ON DELETE CASCADE,
    submitted_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
) INHERITS (public.answers);
