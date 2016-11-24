-- https://leetcode.com/problems/rising-temperature/

-- Given a Weather table, write a SQL query to find all dates' 
-- Ids with higher temperature compared to its previous (yesterday's) dates.

-- +---------+------------+------------------+
-- | Id(INT) | Date(DATE) | Temperature(INT) |
-- +---------+------------+------------------+
-- |       1 | 2015-01-01 |               10 |
-- |       2 | 2015-01-02 |               25 |
-- |       3 | 2015-01-03 |               20 |
-- |       4 | 2015-01-04 |               30 |
-- +---------+------------+------------------+
-- For example, return the following Ids for the above Weather table:
-- +----+
-- | Id |
-- +----+
-- |  2 |
-- |  4 |
-- +----+



SELECT t1.Id 
FROM Weather as t1, Weather as t2
WHERE TO_DAYS(t1.Date) = TO_DAYS(t2.Date) + 1
AND t1.Temperature > t2.Temperature
