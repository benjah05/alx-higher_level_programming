-- Not my genre
SELECT tv_genres.name AS name FROM tv_genres
WHERE tv_genres.id NOT IN (
	SELECT tv_show_genres.genre_id FROM tv_show_genres
	INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
	WHERE tv_shows.title = 'Dexter'
)
ORDER BY name ASC;
