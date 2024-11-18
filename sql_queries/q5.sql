-- srednia ocen w kursach

SELECT 
    c.title AS course_title,
    ROUND(AVG(s.grade), 2) AS average_grade
FROM 
    courses c
JOIN 
    groups g ON c.id = g.course_id
JOIN 
    entries e ON g.id = e.group_id
JOIN 
    exercises ex ON e.id = ex.entry_id
JOIN 
    solutions s ON ex.id = s.exercise_id
GROUP BY 
    c.title
ORDER BY 
    average_grade DESC;