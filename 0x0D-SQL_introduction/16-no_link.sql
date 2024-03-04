-- to list all recordes of second_table in order (score, name)
-- in descending order

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC
;
