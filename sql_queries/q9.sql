-- Srednia ocena i liczba rozwiazywanych testow przez studentow
-- ktorzy rozwiazali wiecej niz 5 zadan i maja srednia ocen powyzej 3.60

SELECT 
    s.student_id,
    u.first_name,
    u.surname,
    AVG(s.grade) AS avg_grade,
    COUNT(s.exercise_id) AS num_tests
FROM 
    public.solutions s
JOIN 
    public.users u ON s.student_id = u.id
GROUP BY 
    s.student_id,
	u.id
HAVING 
    COUNT(s.exercise_id) > 5 AND AVG(s.grade) > 3.60;