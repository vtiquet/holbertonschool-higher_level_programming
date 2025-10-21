-- a script that computes the score average of all records in the table second_table
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;