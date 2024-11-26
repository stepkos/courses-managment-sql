-- FK user_id
CREATE INDEX idx_courses_created_by ON public.courses(created_by);
CREATE INDEX idx_groups_created_by ON public.groups(created_by);
CREATE INDEX idx_student_groups_student_id ON public.student_groups(student_id);
CREATE INDEX idx_student_groups_created_by ON public.student_groups(created_by);
CREATE INDEX idx_host_groups_host_id ON public.host_groups(host_id);
CREATE INDEX idx_host_courses_host_id ON public.host_courses(host_id);
CREATE INDEX idx_host_courses_created_by ON public.host_courses(created_by);
CREATE INDEX idx_entries_host_id ON public.entries(host_id);
CREATE INDEX solutions_student_id ON public.solutions(student_id);
CREATE INDEX idx_attempts_student_id ON public.attempts(student_id);

-- FK entries
CREATE INDEX idx_comment_of_entries_entry_id ON public.comment_of_entries(entry_id);
CREATE INDEX idx_entry_files_entry_id ON public.entry_files(entry_id);
CREATE INDEX idx_exercises_entry_id ON public.exercises(entry_id);
CREATE INDEX idx_tests_entry_id ON public.tests(entry_id);

-- FK tests
CREATE INDEX idx_attempts_test_id ON public.attempts(test_id);
CREATE INDEX idx_open_questions_test_id ON public.open_questions(test_id);
CREATE INDEX idx_closed_questions_test_id ON public.closed_questions(test_id);

-- user.email
CREATE INDEX idx_user_email ON public.users(email);



-- OPTYMALIZACJA KONKRETNYCH ZAPYTAŃ

-- 1)
-- CREATE INDEX idx_attempts_score ON attempts (score);

-- 2)
-- CREATE INDEX idx_choices_closed_question_id ON choices (closed_question_id);
-- CREATE INDEX idx_tests_entry_id ON tests (entry_id);
-- CREATE INDEX idx_entries_title ON entries (title);
