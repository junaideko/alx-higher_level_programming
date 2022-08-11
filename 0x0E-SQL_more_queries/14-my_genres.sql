-- Script uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- The record display: tv_genres.name
-- Results sorted in ascending order by the genre name
-- Only one SELECT statement can be used andThe database name is passed as an argument of the mysql command
SELECT tv_genres.name
FROM tv_genres 
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
