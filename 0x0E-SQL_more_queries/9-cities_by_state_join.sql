-- Lists all cities contained in the database hbtn_0d_usa.
-- Each record display: cities.id - cities.name - states.name
-- Results is sorted in ascending order by cities.id
-- only one SELECT statement is used and database name is passed as an argument of the mysql command
SELECT cities.id, cities.name, states.name
FROM cities INNER JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;
