-- script that lists the number of records with the same score in the table
-- Records are in descending order
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
