/*SELECT BASICS*/

-- The example uses a WHERE clause to show the population of 'France'. Note that strings (pieces of text that are data) should be in 'single quotes'. Modify it to show the population of Germany
SELECT population FROM world
  WHERE name = 'Germany'

-- Checking a list The word IN allows us to check if an item is in a list. The example shows the name and population for the countries 'Brazil', 'Russia', 'India' and 'China'. Show the name and the population for 'Sweden', 'Norway' and 'Denmark'.
SELECT name, population FROM world
  WHERE name IN ('Sweden', 'Norway', 'Denmark');

-- Which countries are not too small and not too big? BETWEEN allows range checking (range specified is inclusive of boundary values). The example below shows countries with an area of 250,000-300,000 sq. km. Modify it to show the country and the area for countries with an area between 200,000 and 250,000.
SELECT name, area FROM world
  WHERE area BETWEEN 200000 AND 250000

-- Quiz Answers
-- 1.
SELECT name, population
  FROM world
 WHERE population BETWEEN 1000000 AND 1250000

--  2.  Pick the result you would obtain from this code:
--       SELECT name, population
--       FROM world
--       WHERE name LIKE "Al%"
Table-E

-- 3. Select the code which shows the countries that end in A or L
SELECT name FROM world
 WHERE name LIKE '%a' OR name LIKE '%l'

--  4. Pick the result from the query
-- SELECT name,length(name)
-- FROM world
-- WHERE length(name)=5 and region='Europe'

-- 5. Here are the first few rows of the world table:
-- name	region	area	population	gdp
-- Afghanistan	South Asia	652225	26000000
-- Albania	Europe	28728	3200000	6656000000
-- Algeria	Middle East	2400000	32900000	75012000000
-- Andorra	Europe	468	64000
-- ...
-- Pick the result you would obtain from this code:
-- SELECT name, area*2 FROM world WHERE population = 64000
Andorra	936

-- 6. Select the code that would show the countries with an area larger than 50000 and a population smaller than 10000000
SELECT name, area, population
  FROM world
 WHERE area > 50000 AND population < 10000000

--  7. Select the code that shows the population density of China, Australia, Nigeria and France
SELECT name, population/area
  FROM world
 WHERE name IN ('China', 'Nigeria', 'France', 'Australia')

/*SELECT World Tutorial*/
SELECT name, continent, population FROM world
-- Shows name, continent, population

-- 2. How to use WHERE to filter records. Show the name for the countries that have a population of at least 200 million. 200 million is 200000000, there are eight zeros.
SELECT name FROM world
WHERE population > 200000000

-- 3. Give the name and the per capita GDP for those countries with a population of at least 200 million.
SELECT name, gdp/population
FROM world
WHERE population > 200000000

-- 4. Show the name and population in millions for the countries of the continent 'South America'. Divide the population by 1000000 to get population in millions.
SELECT name, population/1000000
FROM world
WHERE continent IN ('South America')

-- 5. Show the name and population for France, Germany, Italy
SELECT name, population
FROM world
WHERE name IN ('France', 'Germany', 'Italy')

-- 6. Show the countries which have a name that includes the word 'United'
SELECT name
FROM world
WHERE name LIKE 'United%' or name LIKE '%United'

-- 7. Two ways to be big: A country is big if it has an area of more than 3 million sq km or it has a population of more than 250 million.
--
-- Show the countries that are big by area or big by population. Show name, population and area.
SELECT name, population, area
FROM world
WHERE area > 3000000 OR population > 250000000

-- 8. Exclusive OR (XOR). Show the countries that are big by area (more than 3 million) or big by population (more than 250 million) but not both. Show name, population and area.
--
-- Australia has a big area but a small population, it should be included.
-- Indonesia has a big population but a small area, it should be included.
-- China has a big population and big area, it should be excluded.
-- United Kingdom has a small population and a small area, it should be excluded.
SELECT name, population, area
FROM world
WHERE area > 3000000 XOR population > 250000000

-- 9. Show the name and population in millions and the GDP in billions for the countries of the continent 'South America'. Use the ROUND function to show the values to two decimal places.
--
-- For South America show population in millions and GDP in billions both to 2 decimal places.
-- Millions and billions
SELECT name, ROUND(population/1000000, 2), ROUND(gdp/1000000000, 2)
FROM world
WHERE continent IN ('South America')

-- 10. Show the name and per-capita GDP for those countries with a GDP of at least one trillion (1000000000000; that is 12 zeros). Round this value to the nearest 1000.
--
-- Show per-capita GDP for the trillion dollar countries to the nearest $1000.
SELECT name, ROUND(gdp/population, -3)
FROM world
WHERE gdp > 1000000000000

-- 11. Greece has capital Athens.
--
-- Each of the strings 'Greece', and 'Athens' has 6 characters.
--
-- Show the name and capital where the name and the capital have the same number of characters.
--
-- You can use the LENGTH function to find the number of characters in a string

-- Example:
-- SELECT name, LENGTH(name), continent, LENGTH(continent), capital, LENGTH(capital)
--   FROM world
--  WHERE name LIKE 'G%'

SELECT name, capital
  FROM world
 WHERE LENGTH(name) LIKE LENGTH(capital)

-- 12. The capital of Sweden is Stockholm. Both words start with the letter 'S'.
--
-- Show the name and the capital where the first letters of each match. Don't include countries where the name and the capital are the same word.
-- You can use the function LEFT to isolate the first character.
-- You can use <> as the NOT EQUALS operator.

SELECT name, capital
FROM world
WHERE LEFT(name,1) LIKE LEFT(capital,1) AND name <> capital

-- 13. Equatorial Guinea and Dominican Republic have all of the vowels (a e i o u) in the name. They don't count because they have more than one word in the name.
--
-- Find the country that has all the vowels and no spaces in its name.
--
-- You can use the phrase name NOT LIKE '%a%' to exclude characters from your results.
-- The query shown misses countries like Bahamas and Belarus because they contain at least one 'a'

SELECT name
   FROM world
WHERE name LIKE '%a%' AND name LIKE '%e%' AND name LIKE '%i%' AND name LIKE '%o%' AND name LIKE '%u%'
  AND name NOT LIKE '% %'