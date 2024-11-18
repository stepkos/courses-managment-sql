-- Prowadzacy zajecia z wiecej niz jednej grupy

SELECT 
    hc.host_id,
    u.first_name,
    u.surname,
    c.title AS course_title,
    COUNT(DISTINCT hg.group_id) AS group_count
FROM 
    public.host_courses hc
JOIN 
    public.host_groups hg ON hc.host_id = hg.host_id
JOIN 
    public.groups g ON hg.group_id = g.id
JOIN 
    public.users u ON hc.host_id = u.id
JOIN 
    public.courses c ON hc.course_id = c.id
WHERE 
    hc.course_id = g.course_id
GROUP BY 
    hc.host_id, u.first_name, u.surname, c.title
HAVING 
    COUNT(DISTINCT hg.group_id) > 1
ORDER BY 
    group_count DESC;
