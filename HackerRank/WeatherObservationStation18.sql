/*
Query the Manhattan Distance between points P1 and P2 and round it to a scale of 4 decimal places.
Manhattan Distance Definition: The distance between two points measured along axes at right angles. In a plane with p1 at (x1, y1) and p2 at (x2, y2), it is |x1 - x2| + |y1 - y2|.
*/

SELECT ROUND(ABS(MAX(LAT_N) - MIN(LAT_N)) + ABS(MAX(LONG_W) - MIN(LONG_W)), 4) AS "Manhattan Distance" FROM STATION;