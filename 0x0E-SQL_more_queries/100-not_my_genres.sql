-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download
--   Write a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
--	The tv_shows table contains only one record where title = Dexter (but the id can be different)
--	Each record should display: tv_genres.name
--	Results must be sorted in ascending order by the genre name
--	You can use a maximum of two SELECT statement
--	The database name will be passed as an argument of the mysql command

SELECT tv_genres.name
FROM tv_genres
LEFT JOIN (
    SELECT tv_show_genres.genre_id
    FROM tv_show_genres
    INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    WHERE tv_shows.title = 'Dexter'
) AS dexter_genres ON tv_genres.id = dexter_genres.genre_id
WHERE dexter_genres.genre_id IS NULL
ORDER BY tv_genres.name ASC;
