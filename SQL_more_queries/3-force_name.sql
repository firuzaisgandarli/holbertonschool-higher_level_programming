-- 3. Always a name
-- This script creates the table force_name on the MySQL server
-- Table description:
--   id INT
--   name VARCHAR(256) NOT NULL
-- The database name will be passed as an argument of the mysql command
-- If the table force_name already exists, the script will not fail

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
