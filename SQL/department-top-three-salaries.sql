-- https://leetcode.com/problems/department-top-three-salaries/

-- The Employee table holds all employees. Every employee has an Id, 
-- and there is also a column for the department Id.

-- +----+-------+--------+--------------+
-- | Id | Name  | Salary | DepartmentId |
-- +----+-------+--------+--------------+
-- | 1  | Joe   | 70000  | 1            |
-- | 2  | Henry | 80000  | 2            |
-- | 3  | Sam   | 60000  | 2            |
-- | 4  | Max   | 90000  | 1            |
-- | 5  | Janet | 69000  | 1            |
-- | 6  | Randy | 85000  | 1            |
-- +----+-------+--------+--------------+
-- The Department table holds all departments of the company.

-- +----+----------+
-- | Id | Name     |
-- +----+----------+
-- | 1  | IT       |
-- | 2  | Sales    |
-- +----+----------+
-- Write a SQL query to find employees who earn the top three salaries in 
-- each of the department. For the above tables, your SQL query should 
-- return the following rows.

-- +------------+----------+--------+
-- | Department | Employee | Salary |
-- +------------+----------+--------+
-- | IT         | Max      | 90000  |
-- | IT         | Randy    | 85000  |
-- | IT         | Joe      | 70000  |
-- | Sales      | Henry    | 80000  |
-- | Sales      | Sam      | 60000  |
-- +------------+----------+--------+



SELECT t2.Name as Department, t1.Name as Employee, t1.Salary as Salary
FROM Employee as t1, Department as t2
WHERE t1.DepartmentId = t2.Id
AND 3 > (
      SELECT COUNT(DISTINCT(t3.Salary)) FROM Employee as t3
      WHERE t3.Salary > t1.Salary 
      AND t3.DepartmentId = t1.DepartmentId
  )




-- select D.Name as Department, t.Name as Employee, t.Salary as Salary
-- from
-- (
--     select Name, 
--            Salary,
--            DepartmentId,
--            (
--                case when @prev_departId <> (@prev_departId := DepartmentId) then @rank := ((@prev_salary := Salary) = Salary)
--                     when @prev_salary <> (@prev_salary := Salary) then @rank := @rank + 1
--                     else @rank
--                end
--            ) as rank
--     from
--     (
--         select *
--         from Employee 
--         order by DepartmentId, Salary desc
--     ) A, (select @rank := 0, @prev_departId := -1, @prev_salary := -1) Init
-- ) t, Department D
-- where t.rank in (1, 2, 3) and t.DepartmentId = D.Id