-- lists all the cities of california in the database
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = state_id 
    AND state.name = 'California'
ORDER BY cities.id ASC;
