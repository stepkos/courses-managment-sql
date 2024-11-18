-- TODO: Solution nie jest jakkolwiek polaczony z testem
-- wystarczy tylko tabela attempt ktora trzyma scory dla podejsc do testow
-- dla studentow. Trzeba wymyslic cos innego, trudniejszego.

-- Studenci z co najmniej trzema ocenami powyzej 4 z testow


SELECT 
    s.student_id,
    u.first_name,
    u.surname,
    COUNT(t.id) AS num_tests_above_4
FROM 
    public.solutions s
JOIN 
    public.exercises e ON s.exercise_id = e.id
JOIN 
    public.entries en ON e.entry_id = en.id
JOIN 
    public.tests t ON en.id = t.entry_id
JOIN 
    public.users u ON s.student_id = u.id  
WHERE 
    s.grade > 4
GROUP BY 
    s.student_id, u.id
HAVING 
    COUNT(t.id) >= 3
ORDER BY 
    num_tests_above_4 DESC;