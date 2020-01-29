/*
Write a query to output the names of those students whose best friends got offered a higher salary than them. Names must be ordered by the salary amount offered to the best friends. It is guaranteed that no two students got same salary offer.
*/

SELECT S.name
FROM (students as S JOIN friends as F USING(id)
INNER JOIN packages AS PS ON S.id = PS.id
INNER JOIN packages AS PF ON F.friend_id = PF.id)
WHERE PF.salary > PS.salary
ORDER BY PF.salary;