-- 11. Select the best
-- This script lists all records with score >= 10
-- from the table second_table of the database hbtn_0c_0
-- Results display both the score and the name (in this order)
-- Records are ordered by score (top first)

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
