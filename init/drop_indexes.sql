DROP INDEX idx_courses_created_by;
DROP INDEX idx_groups_created_by;
DROP INDEX idx_student_groups_student_id;
DROP INDEX idx_student_groups_created_by;
DROP INDEX idx_host_groups_host_id;
DROP INDEX idx_host_courses_host_id;
DROP INDEX idx_host_courses_created_by;
DROP INDEX idx_entries_host_id;
DROP INDEX solutions_student_id;
DROP INDEX idx_attempts_student_id;

DROP INDEX idx_comment_of_entries_entry_id;
DROP INDEX idx_entry_files_entry_id;
DROP INDEX idx_exercises_entry_id;
DROP INDEX idx_tests_entry_id;

DROP INDEX idx_attempts_test_id;
DROP INDEX idx_open_questions_test_id;
DROP INDEX idx_closed_questions_test_id;

DROP INDEX idx_user_email;

-- OPTYMALIZACJA KONKRETNYCH ZAPYTAŃ

-- 1)
-- DROP INDEX idx_attempts_score;

-- 2)
-- DROP INDEX idx_choices_closed_question_id;
-- DROP INDEX idx_tests_entry_id;
-- DROP INDEX idx_entries_title;

