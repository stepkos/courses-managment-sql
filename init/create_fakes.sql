INSERT INTO public.administrators (first_name, surname, email, password, is_active)
VALUES ('Admin', 'User', 'admin.user@example.com', 'adminpassword', TRUE);

INSERT INTO public.faculties (name, email, phone, website)
VALUES ('Faculty of Science', 'science@example.com', '+1 234567890', 'http://facultywebsite.com');

INSERT INTO public.faculty_administrators (faculty_id, administrator_id)
VALUES (1, 1);

INSERT INTO public.fields_of_study (name, faculty_id, description, start_year)
VALUES ('Computer Science', 1, DEFAULT, 2021);

INSERT INTO public.terms (field_of_study_id, term_number)
VALUES (1, 1);

INSERT INTO public.courses (term_id, title, description)
VALUES (1, 'Introduction to Programming', 'Basic programming concepts and techniques.');

INSERT INTO public.college_terms (start_date, end_date)
VALUES (NOW(), NOW() + INTERVAL '4 months');

INSERT INTO public.degrees (id, name) VALUES (1, 'PhD');

INSERT INTO public.hosts (first_name, surname, email, password, is_active, degree)
VALUES ('Host', 'User', 'host.user@example.com', 'hostpassword', TRUE, 1);

INSERT INTO public.groups (course_id, college_term_id, name, description, image, created_by, created_at)
VALUES (1, 1, 'Group A', 'Description of Group A', 'http://example.com/image.jpg', 1, NOW());

INSERT INTO public.students (first_name, surname, email, password, is_active)
VALUES ('Student', 'User', 'student.user@example.com', 'studentpassword', TRUE);

INSERT INTO public.student_groups (group_id, student_id, created_by, created_at)
VALUES (1, 1, 1, NOW());

INSERT INTO public.host_groups (host_id, group_id)
VALUES (1, 1);

INSERT INTO public.host_courses (host_id, course_id, is_course_admin, created_by, created_at)
VALUES (1, 1, TRUE, 1, NOW());

INSERT INTO public.entries (group_id, title, created_at, updated_at, content, host_id)
VALUES (1, 'Entry Title', NOW(), NOW(), 'Content of the entry', 1);

INSERT INTO public.comment_of_entries (commenter_id, commenter_type, content, created_at, entry_id)
VALUES (1, 1, 'Comment content', NOW(), 1);

INSERT INTO public.entry_files (entry_id, file_url, uploaded_at)
VALUES (1, 'http://example.com/file.pdf', NOW());

INSERT INTO public.exercises (entry_id, due_date)
VALUES (1, NOW() + INTERVAL '7 days');

INSERT INTO public.solutions (exercise_id, student_id, grade, submitted_at, text_answer)
VALUES (1, 1, 9, NOW(), 'Solution text');

INSERT INTO public.solution_files (solution_id, file_url, uploaded_at)
VALUES (1, 'http://example.com/solutionfile.pdf', NOW());

INSERT INTO public.solution_comments (commenter_id, commenter_type, solution_id, content, created_at)
VALUES (1, 1, 1, 'Comment on solution', NOW());

INSERT INTO public.tests (entry_id, title, description, available_from_date, available_to_date, max_seconds_for_open, max_seconds_for_closed, duration_in_minutes, created_at, updated_at)
VALUES (1, 'Test Title', 'Description of the test', NOW(), NOW() + INTERVAL '1 day', 600, 300, 60, NOW(), NOW());

INSERT INTO public.attempts (student_id, test_id, score, started_at, submitted_at)
VALUES (1, 1, 85, NOW(), NOW());

INSERT INTO public.open_questions (test_id, content, points)
VALUES (1, 'Describe the main components of a computer.', 10);

INSERT INTO public.closed_questions (test_id, is_multiple, content, points)
VALUES (1, TRUE, 'What is the capital of France?', 5);

INSERT INTO public.choices (closed_question_id, content, is_correct)
VALUES (1, 'Paris', TRUE);

INSERT INTO public.closed_answers (attempt_id, closed_question_id, submitted_at)
VALUES (1, 1, NOW());

INSERT INTO public.closed_answer_choices (closed_answer_id, choice_id)
VALUES (1, 1);

INSERT INTO public.open_answers (open_question_id, content, attempt_id, submitted_at)
VALUES (1, 'The main components of a computer are the CPU, memory, and storage.', 1, NOW());
