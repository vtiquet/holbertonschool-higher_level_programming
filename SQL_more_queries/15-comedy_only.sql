-- Lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT
    t.title
FROM
    tv_shows AS t
INNER JOIN
    tv_show_genres AS sg
ON
    t.id = sg.show_id
INNER JOIN
    tv_genres AS g
ON
    sg.genre_id = g.id
WHERE
    g.name = 'Comedy'
ORDER BY
    t.title ASC;
