-- Srednia ocen z danego testu

SELECT 
    t.id AS test_id,
    t.title, 
    AVG(a.score) AS avg_score
FROM 
    public.attempts a
JOIN 
    public.tests t ON a.test_id = t.id
GROUP BY 
    t.id
HAVING 
    COUNT(a.id) > 5 -- Test musi mieć co najmniej 5 prób, aby zostać uwzględnionym
ORDER BY 
    avg_score ASC;