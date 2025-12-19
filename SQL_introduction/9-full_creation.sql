-- 9. Full creation
-- This script creates a table called second_table in the database hbtn_0c_0
-- The table has three columns: id (INT), name (VARCHAR(256)), score (INT)
-- If the table already exists, the script will not fail
-- It also inserts multiple rows into the table

CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10);
INSERT INTO second_table (id, name, score) VALUES (2, 'Alex', 3);
INSERT INTO second_table (id, name, score) VALUES (3, 'Bob', 14);
INSERT INTO second_table (id, name, score) VALUES (4, 'George', 8);
