-- Script lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record display: <TV Show genre> - <Number of shows linked to this genre>
-- First column is called genre and Second column is called number_of_shows
-- Doesn’t display a genre that doesn’t have any shows linked
-- Results sorted in descending order by the number of shows linked
-- Only one SELECT statement and database name is passed as an argument of the mysql command
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
