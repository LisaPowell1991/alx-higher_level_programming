-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download
--  Write a script that uses the hbtn_0d_tvshows database to lists all Comedies
--	Each record should display: tv_shows.title
--	Results must be sorted in ascending order by the show title
--	You can use only one SELECT statement
--	The database name will be passed as an argument of the mysql command

SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
