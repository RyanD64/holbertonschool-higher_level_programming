-- list all genres by their ratings
SELECT `title`, SUM(`rate`) AS `rating`
FROM `tv_genres`
INNER JOIN `tv_show_genres` ON tv_shows_genres.`genres_id` = tv_genres.`id`
INNER JOIN `tv_show_ratings` ON tv_shows_ratings.`show_id` = tv_show_genres.`show_id`
GROUP BY `name`
ORDER BY SUM(`rate`) DESC;