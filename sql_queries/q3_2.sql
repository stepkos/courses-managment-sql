-- hosty ktore nie sa przypisane do kursu zadnego
SELECT 
    g.name AS group_name,
    c.title AS course_title
FROM 
    groups g
JOIN 
    courses c ON g.course_id = c.id
LEFT JOIN 
    host_groups hg ON g.id = hg.group_id
WHERE 
    hg.host_id IS NULL;