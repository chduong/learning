/*
Given the table schemas, write a query to print the company_code, founder name, total number of lead managers, total number of senior managers, total number of managers, and total number of employees. Order your output by ascending company_code.
*/

SELECT C.company_code, C.founder,
(SELECT COUNT(DISTINCT lead_manager_code) FROM Lead_Manager WHERE company_code = C.company_code),
(SELECT COUNT(DISTINCT senior_manager_code) FROM Senior_Manager WHERE company_code = C.company_code),
(SELECT COUNT(DISTINCT manager_code) FROM Manager WHERE company_code = C.company_code),
(SELECT COUNT(DISTINCT employee_code) FROM Employee WHERE company_code = C.company_code)
FROM Company AS C ORDER BY C.company_code;

/*
SELECT c.company_code, c.founder,
(SELECT count(distinct lead_manager_code) FROM Lead_Manager WHERE company_code = c.company_code),
(SELECT count(distinct senior_manager_code) FROM Senior_Manager WHERE company_code = c.company_code),
(SELECT count(distinct manager_code) FROM Manager WHERE company_code = c.company_code),
(SELECT count(distinct employee_code) FROM Employee WHERE company_code = c.company_code)
FROM Company AS c ORDER BY c.company_code;
*/

/*
select c.company_code, c.founder,
    count(distinct l.lead_manager_code), count(distinct s.senior_manager_code),
    count(distinct m.manager_code),count(distinct e.employee_code)
from Company c, Lead_Manager l, Senior_Manager s, Manager m, Employee e
where c.company_code = l.company_code
    and l.lead_manager_code=s.lead_manager_code
    and s.senior_manager_code=m.senior_manager_code
    and m.manager_code=e.manager_code
group by c.company_code order by c.company_code;
 */