-- 9-cities_by_state_join
-- Displays all cities in the database hbtn_0d_usa
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON cities.state_id = states.id;
