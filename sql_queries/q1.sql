SELECT 
    u.first_name, 
    u.surname, 
    AVG(s.grade) AS avg_grade
FROM 
    public.solutions s
JOIN 
    public.users u ON s.student_id = u.id
GROUP BY 
    u.id, u.first_name, u.surname
ORDER BY 
    avg_grade DESC
LIMIT 10;