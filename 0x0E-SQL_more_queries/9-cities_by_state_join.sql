-- Script that lists all the cities contained in the database hbtn_0d_usa
-- Each record displays: cities.id - cities.name - states.name
-- Results are sorted in ascending order by cities.id
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
