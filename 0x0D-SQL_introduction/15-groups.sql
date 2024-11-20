-- Number by score
SELECT score, COUNT(*) As number FROM second_table
GROUP BY score ORDER BY number DESC;
