-- 10. List by best
-- This script lists all records of the table second_table
-- from the database hbtn_0c_0 in the MySQL server
-- Results display both the score and the name (in this order)
-- Records are ordered by score (top first)

SELECT score, name FROM second_table ORDER BY score DESC;
