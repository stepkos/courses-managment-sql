-- Liczba studentow przypisanych do kazdej grupy

SELECT 
    g.name AS group_name,
    c.title AS course_title,
    COUNT(sg.student_id) AS num_students
FROM 
    public.student_groups sg
JOIN 
    public.groups g ON sg.group_id = g.id
JOIN 
    public.courses c ON g.course_id = c.id
GROUP BY 
    g.id, c.id
ORDER BY 
    num_students DESC, g.name;