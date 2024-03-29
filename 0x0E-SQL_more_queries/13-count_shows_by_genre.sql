-- Script that lists all genres from hbtn_0d_tvshows and displays
-- the number of shows linked to each
-- Each record displays: <TV Show genre> - <Number of shows linked to this genre>
-- First column called genre, Second column called number_of_shows
-- Results are sorted in descending order by the number of shows linked
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_shows_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
