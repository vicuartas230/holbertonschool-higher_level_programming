-- This script lists all shows contained in the database hbtn_0d_tvshows.
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows FULL JOIN tv_show_genres ON tv_show_genres.show_id=tv_shows.id WHERE tv_shows.title IS NULL OR tv_show_genres.genre_id IS NULL ORDER BY tv_shows.title, tv_show_genres.genre_id;
