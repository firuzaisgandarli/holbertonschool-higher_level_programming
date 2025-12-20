-- 8. Cities of California
-- This script lists all the cities of California from the database hbtn_0d_usa
-- The states table contains only one record where name = 'California'
-- Results must be sorted in ascending order by cities.id
-- The query must not use the JOIN keyword

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;
