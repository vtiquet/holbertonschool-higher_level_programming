-- Lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT
    t.title,
    sg.genre_id
FROM
    tv_shows AS t
LEFT JOIN
    tv_show_genres AS sg
ON
    t.id = sg.show_id
WHERE
    sg.genre_id IS NULL
ORDER BY
    t.title ASC,
    sg.genre_id ASC;
