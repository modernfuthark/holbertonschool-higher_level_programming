-- 5-unqiue_id
-- Creates a table 'unique_id' where the ID defaults to a unique value
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256) NOT NULL);
