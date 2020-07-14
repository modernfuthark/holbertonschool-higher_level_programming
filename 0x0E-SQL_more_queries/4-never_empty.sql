-- 4-never_empty
-- Creates a table 'id_not_null' with id's default value being '1'
CREATE TABLE IF NOT NULL id_not_null (id INT DEFAULT 1, name VARCHAR(256) NOT NULL);
