-- 8-cities_of_california_subquery
-- lists all cities of California that can be found in the database
SELECT id, name from cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY cities.id ASC;
