-- Script that lists all uses the hbtn_0d_tvshows database to
-- lists all genres of the show Dexter
-- Each record displays: tv_genres.name
-- Results are sorted in descending order by the genre name
SELECT tv_genres.name
FROM tv_genres
JOIN tv_shows_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_show.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
