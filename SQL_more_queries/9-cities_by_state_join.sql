-- Lists all cities with their states using a JOIN.
SELECT
    c.id,
    c.name,
    s.name
FROM
    cities AS c
INNER JOIN
    states AS s
ON
    c.state_id = s.id
ORDER BY
    c.id ASC;
