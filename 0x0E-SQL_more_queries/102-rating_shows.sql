-- Script that lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record displays: tv_shows.title - rating sum
-- Results are sorted in ascending order by the rating
SELECT tv_shows.title, SUM(hbtn_0d_tvshows_rate.rating) AS rating_sum
FROM tv_shows
JOIN  hbtn_0d_tvshows_rate ON tv_shows.id = hbtn_0d_tvshows_rate.show_iGROUP BY tv_shows.title ASC;
GROUP BY tv_shows.title;
ORDER BY rating_sum DESC;
