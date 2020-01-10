/*Case Statements*/
-- Example 1:
SELECT player_name,
       year,
       CASE WHEN year = 'SR' THEN 'yes'
            ELSE NULL END AS is_a_senior
  FROM benn.college_football_players

-- 1. The CASE statement checks each row to see if the conditional statement - year = 'SR' is true.
-- 2. For any given row, if that conditional statement is true, the word 'yes' gets printed in the column that we have named is_a_senior.
-- 3. In any row for which the condiational statement is false, nothing happens to that row and a null value is left in the is_a_senior column.
-- 4. At the same time all of this is happening, SQL is retrieving and displaying all the values in the player_name and year columns.

-- Example 2 Replace Null with 'no' for a column:
SELECT player_name,
       year,
       CASE WHEN year = 'SR' THEN 'yes'
            ELSE 'no' END AS is_a_senior
  FROM benn.college_football_players

-- Example 3. Adding multiple conditions to a CASE statement:
SELECT player_name,
       weight,
       CASE WHEN weight > 250 THEN 'over 250'
            WHEN weight > 200 THEN '201-250'
            WHEN weight > 175 THEN '176-200'
            ELSE '175 or under' END AS weight_group
  FROM benn.college_football_players

-- Example 4. Giving a range between conditions to a CASE statement:
SELECT player_name,
       weight,
       CASE WHEN weight > 250 THEN 'over 250'
            WHEN weight > 200 AND weight <= 250 THEN '201-250'
            WHEN weight > 175 AND weight <= 200 THEN '176-200'
            ELSE '175 or under' END AS weight_group
  FROM benn.college_football_players

-- Example 5. Stringing together multiple condition statements with AND, OR:
SELECT player_name,
       CASE WHEN year = 'FR' AND position = 'WR' THEN 'frosh_wr'
            ELSE NULL END AS sample_case_statement
  FROM benn.college_football_players

-- Review:
-- 1. The CASE statement always goes in the SELECT clause
-- 2. CASE must include the following components: WHEN, THEN, and END. ELSE is an optional component.
-- 3. You can make any conditional statement using any conditional operator (like WHERE ) between WHEN and THEN. This includes stringing together multiple conditional statements using AND and OR.
-- 4. You can include multiple WHEN statements, as well as an ELSE statement to deal with any unaddressed conditions.

-- Using CASE with aggregate functions (SUM, MIN, MAX, COUNT, AVG):
-- Example 1:
SELECT CASE WHEN year = 'FR' THEN 'FR'
            ELSE 'Not FR' END AS year_group,
            COUNT(1) AS count
  FROM benn.college_football_players
 GROUP BY CASE WHEN year = 'FR' THEN 'FR'
               ELSE 'Not FR' END

-- Example 2:
SELECT COUNT(1) AS fr_count
  FROM benn.college_football_players
 WHERE year = 'FR'

-- Example 3, filter by everything that was counted as 1:
SELECT CASE WHEN year = 'FR' THEN 'FR'
            WHEN year = 'SO' THEN 'SO'
            WHEN year = 'JR' THEN 'JR'
            WHEN year = 'SR' THEN 'SR'
            ELSE 'No Year Data' END AS year_group,
            COUNT(1) AS count
  FROM benn.college_football_players
 GROUP BY 1

--  Example 4, filter by year_group:
 SELECT CASE WHEN year = 'FR' THEN 'FR'
            WHEN year = 'SO' THEN 'SO'
            WHEN year = 'JR' THEN 'JR'
            WHEN year = 'SR' THEN 'SR'
            ELSE 'No Year Data' END AS year_group,
            COUNT(1) AS count
  FROM benn.college_football_players
 GROUP BY year_group

--  Example 5. Using CASE inside of aggregate functions:
 SELECT CASE WHEN year = 'FR' THEN 'FR'
            WHEN year = 'SO' THEN 'SO'
            WHEN year = 'JR' THEN 'JR'
            WHEN year = 'SR' THEN 'SR'
            ELSE 'No Year Data' END AS year_group,
            COUNT(1) AS count
  FROM benn.college_football_players
 GROUP BY 1