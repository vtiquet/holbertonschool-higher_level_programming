-- Lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT
    t.title,
    g.name
FROM
    tv_shows AS t
LEFT JOIN
    tv_show_genres AS sg
ON
    t.id = sg.show_id
LEFT JOIN
    tv_genres AS g
ON
    sg.genre_id = g.id
ORDER BY
    t.title ASC,
    g.name ASC;
