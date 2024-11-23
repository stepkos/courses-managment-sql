-- Liczba kursow kazdego hosta

SELECT host_id, first_name, surname, num_courses
FROM (
    SELECT 
        u.id AS host_id, 
		u.first_name, 
		u.surname,
        COUNT(hc.id) AS num_courses
    FROM 
        public.users u
    JOIN 
        public.host_courses hc ON u.id = hc.host_id
    GROUP BY 
        u.id
) subquery
WHERE num_courses > 1
ORDER BY num_courses DESC
LIMIT 10;