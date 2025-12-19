-- 16. Say my name
-- This script lists all records of the table second_table
-- from the database hbtn_0c_0 in the MySQL server
-- It does not list rows where the name column is empty or NULL
-- Results display score and name (in this order)
-- Records are listed by descending score

SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
