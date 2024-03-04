-- to list num of recordes with same score in second_table

SELECT score, COUNT(score)
AS number
From second_table
GROUP BY score
ORDER BY number DESC
;
