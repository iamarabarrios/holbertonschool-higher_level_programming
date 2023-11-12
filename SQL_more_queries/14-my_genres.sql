-- Import the database dump from hbtn_0d_tvshows.
SELECT tg.name
FROM tv_shows AS ts
JOIN tv_show_genres AS tsg ON ts.id = tsg.show_id
JOIN tv_genres AS tg ON tsg.genre_id = tg.id
WHERE ts.title = "Dexter"
ORDER BY tg.name ASC;
