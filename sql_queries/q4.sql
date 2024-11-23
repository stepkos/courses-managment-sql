-- Procent studentow w grupie wzgledem ogolu

WITH total_students AS (
    SELECT COUNT(DISTINCT student_id) AS total FROM public.student_groups
)
SELECT 
    g.name AS group_name, 
    COUNT(sg.student_id) AS num_students, 
    ROUND(COUNT(sg.student_id) * 100.0 / ts.total, 2) AS percentage
FROM 
    public.student_groups sg
JOIN 
    public.groups g ON sg.group_id = g.id
CROSS JOIN 
    total_students ts
GROUP BY 
    g.id, g.name, ts.total
ORDER BY 
    percentage DESC
LIMIT 50;