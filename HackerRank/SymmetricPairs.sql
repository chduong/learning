/*
Two pairs (X1, Y1) and (X2, Y2) are said to be symmetric pairs if X1 = Y2 and X2 = Y1.
Write a query to output all such symmetric pairs in ascending order by the value of X.
*/

/* Not all versions of SQL have ROWID
SELECT DISTINCT A.x, A.y
FROM functions AS A
WHERE (
    SELECT COUNT(*)
    FROM functions AS B
    WHERE A.x = B.y AND A.y = B.x AND A.ROWID != B.ROWID
          ) > 0
AND A.x <= A.y
ORDER BY A.x ASC
*/

SELECT DISTINCT F1.x, F1.y
FROM functions AS F1
INNER JOIN functions AS F2 ON F1.x = F2.y AND F1.y = F2.x /* Obtains symmetric pairs defined by problem */
GROUP BY F1.x, F1.y
HAVING COUNT(F1.x) > 1 or F1.x < F1.y
ORDER BY F1.x