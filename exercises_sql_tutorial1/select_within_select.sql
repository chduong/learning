-- DATABASE:
-- name	continent	area	population	gdp
-- Afghanistan	Asia	652230	25500100	20343000000
-- Albania	Europe	28748	2831741	12960000000
-- Algeria	Africa	2381741	37100000	188681000000
-- Andorra	Europe	468	78115	3712000000
-- Angola	Africa	1246700	20609294	100990000000
-- ...

-- 1. List each country name where the population is larger than that of 'Russia'.
--
-- world(name, continent, area, population, gdp)
SELECT name FROM world
    WHERE population >
        (SELECT population FROM world
        WHERE name ='Russia')

-- 2. Show the countries in Europe with a per capita GDP greater than 'United Kingdom'.
--
-- Per Capita GDP: The per capita GDP is the gdp/population
SELECT name FROM world
    WHERE continent = 'Europe'
    AND gdp/population >
        (SELECT gdp/population FROM world
        WHERE name = 'United Kingdom')

-- 3. List the name and continent of countries in the continents containing either Argentina or Australia. Order by name of the country.
SELECT name, continent FROM world
    WHERE continent = 'South America'
    OR continent = 'Oceania'
    ORDER BY name

-- 4. Which country has a population that is more than Canada but less than Poland? Show the name and the population.
SELECT name, population FROM world
    WHERE population <
        (SELECT population FROM world
        WHERE name = 'Poland')
    AND population >
        (SELECT population FROM world
        WHERE name = 'Canada')

-- 5. Germany (population 80 million) has the largest population of the countries in Europe. Austria (population 8.5 million) has 11% of the population of Germany.
--
-- Show the name and the population of each country in Europe. Show the population as a percentage of the population of Germany.
--
-- Decimal places: You can use the function ROUND to remove the decimal places.
-- Percent symbol %: You can use the function CONCAT to add the percentage symbol.
SELECT name, CONCAT(ROUND(100 * population / (SELECT population
                                                FROM world
                                                WHERE name = 'Germany')), '%')
FROM world
WHERE continent = 'Europe'

-- Side note:
-- We can use the word ALL to allow >= or > or < or <=to act over a list. For example, you can find the largest country in the world, by population with this query:
--
-- SELECT name
--   FROM world
--  WHERE population >= ALL(SELECT population
--                            FROM world
--                           WHERE population>0)

-- 6. Which countries have a GDP greater than every country in Europe? [Give the name only.] (Some countries may have NULL gdp values)
SELECT name FROM world
    WHERE gdp > ALL
        (SELECT gdp FROM world
        WHERE continent = 'Europe' AND gdp IS NOT NULL)

-- 7. Find the largest country (by area) in each continent, show the continent, the name and the area:
-- Given:
-- SELECT continent, name, population FROM world x
--   WHERE population >= ALL
--     (SELECT population FROM world y
--         WHERE y.continent=x.continent
--           AND population>0)
SELECT continent, name, area FROM world x
    WHERE area >= ALL
        (SELECT area FROM world y
            WHERE y.continent=x.continent
            AND y.area >= x.area)