-- Najwyzsze srednie oceny
SELECT 
    u.id AS "user_id",
    u.first_name, 
    u.surname, 
    ROUND(AVG(s.grade), 2) AS avg_grade
FROM 
    public.solutions s
JOIN 
    public.users u ON s.student_id = u.id
GROUP BY 
    u.id
ORDER BY 
    avg_grade DESC
LIMIT 10;