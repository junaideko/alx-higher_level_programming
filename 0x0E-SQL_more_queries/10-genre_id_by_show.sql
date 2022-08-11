-- Import the database dump from hbtn_0d_tvshows to your MySQL server(how to do this is in my readme.md file
-- Script lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Each record is displayed as: tv_shows.title - tv_show_genres.genre_id
-- Results is sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- Only one SELECT statement is used and database name is  passed as an argument of the mysql command
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
