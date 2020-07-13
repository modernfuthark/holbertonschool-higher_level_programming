-- 15-groups
-- Lists the number of different scores in table 'second_table'
SELECT score, count(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
