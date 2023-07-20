-- Script that lists all genres in the database hbtn_0d_tvshows_rate by their rating
-- Each record displays: tv_genres.name - rating sum
-- Results are sorted in ascending order by the rating
SELECT tv_genres.name, SUM(hbtn_0d_tvshows_rate.rating) AS rating_sum
FROM tv_genres
LEFT JOIN  (
	SELECT tv_show_genres.genre_id, hbtn_0d_tvshows_rate.rating
	FROM tv_show_genres
	JOIN hbtn_0d_tvshows_rate ON tv_show_genres.show_id = hbtn_0d_tvshows_rate.show_id
) AS genre_ratings ON tv_genre.id = genre_ratings.genre_id
GROUP BY tv_genres.name;
ORDER BY rating_sum DESC;
