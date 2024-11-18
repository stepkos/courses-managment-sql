-- najpopularniejsze odpowiedzi do pytan zamknietych

SELECT 
    cq.content AS question_content,
    ch.content AS choice_content,
    COUNT(cac.id) AS times_chosen,
	ch.is_correct AS choice_is_correct
FROM 
    closed_questions cq
JOIN 
    choices ch ON cq.id = ch.closed_question_id
LEFT JOIN 
    closed_answer_choices cac ON ch.id = cac.choice_id
GROUP BY 
    cq.content, ch.content, ch.is_correct
ORDER BY 
    times_chosen DESC;