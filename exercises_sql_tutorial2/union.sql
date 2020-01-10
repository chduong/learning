-- Joins two data sets:
-- Example 1 for distinct values:
SELECT *
  FROM tutorial.crunchbase_investments_part1

 UNION

 SELECT *
   FROM tutorial.crunchbase_investments_part2

-- Example 2 for all values:
SELECT *
  FROM tutorial.crunchbase_investments_part1

 UNION ALL

 SELECT *
   FROM tutorial.crunchbase_investments_part2