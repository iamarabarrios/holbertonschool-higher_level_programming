-- Import the database dump of hbtn_0d_tvshows.
SELECT ts.title, tsg.genre_id
FROM tv_shows AS ts
LEFT JOIN tv_show_genres AS tsg ON ts.id = tsg.show_id
ORDER BY ts.title, tsg.genre_id ASC;
