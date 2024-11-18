-- grupy, ktore nie mają przypisanego prowadzącego

SELECT 
	g.id AS group_id,
    g.name AS group_name
FROM 
    groups g
LEFT JOIN 
    host_groups hg ON g.id = hg.group_id
LEFT JOIN 
    users u ON u.id = hg.host_id
WHERE
	u.id IS NULL