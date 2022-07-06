-- lists all the cities of california in the database
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = states_id 
    AND states.name = 'California'
ORDER BY cities.id ASC;
