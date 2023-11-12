-- Import the database dump from hbtn_0d_tvshows.
SELECT tg.name AS "genre", COUNT(tsg.show_id) AS "number_of_shows"
FROM tv_genres AS tg
JOIN tv_show_genres AS tsg ON tg.id = tsg.genre_id
JOIN tv_shows AS ts ON tsg.show_id = ts.id
GROUP BY tg.name
ORDER BY number_of_shows DESC;
