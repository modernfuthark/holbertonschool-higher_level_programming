-- 102-avg_temperatures.sql
-- Gets the average temp. of cities by decending temperature
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
