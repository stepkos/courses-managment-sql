-- Liczba ocen danej wartości w danym kursie

SELECT 
    c.id AS course_id,
    c.title AS course_title,
    sol.grade,
    COUNT(sol.id) AS num_grades
FROM 
    public.solutions sol
JOIN 
    public.exercises e ON sol.exercise_id = e.id
JOIN 
    public.entries en ON e.entry_id = en.id
JOIN 
    public.groups g ON en.group_id = g.id
JOIN 
    public.courses c ON g.course_id = c.id
GROUP BY 
    c.id, sol.grade
ORDER BY 
    c.id, sol.grade DESC;