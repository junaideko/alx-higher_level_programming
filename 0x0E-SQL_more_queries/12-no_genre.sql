-- Script lists all shows contained in hbtn_0d_tvshows databasewithout a genre linked.
-- Each record is displayed as: tv_shows.title - tv_show_genres.genre_id
-- Results is sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- Only one SELECT statement is used and database name is  passed as an argument of the mysql command
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id is NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;

