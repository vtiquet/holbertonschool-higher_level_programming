-- Lists all genres of the show Dexter.
SELECT
    g.name
FROM
    tv_genres AS g
INNER JOIN
    tv_show_genres AS sg
ON
    g.id = sg.genre_id
INNER JOIN
    tv_shows AS t
ON
    sg.show_id = t.id
WHERE
    t.title = 'Dexter'
ORDER BY
    g.name ASC;
