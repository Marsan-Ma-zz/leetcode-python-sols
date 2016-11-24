

-- 1. tmp table skill:
SELECT D.Name AS Department ,E.Name AS Employee ,E.Salary 
FROM
    Employee E,
    (SELECT DepartmentId,max(Salary) as max FROM Employee GROUP BY DepartmentId) T,
    Department D
WHERE E.DepartmentId = T.DepartmentId 
  AND E.Salary = T.max
  AND E.DepartmentId = D.id

-- 2. LEFT/RIGHT INNER/OUTER JOIN


-- 3. Nested / EXISTS
SELECT D.Name,A.Name,A.Salary 
FROM 
    Employee A,
    Department D   
WHERE A.DepartmentId = D.Id 
  AND NOT EXISTS 
  (SELECT 1 FROM Employee B WHERE B.Salary > A.Salary AND A.DepartmentId = B.DepartmentId) 


-- 4. use two key as one condition
SELECT D.Name AS Department ,E.Name AS Employee ,E.Salary 
from 
  Employee E,
  Department D 
WHERE E.DepartmentId = D.id 
AND (DepartmentId,Salary) in 
(SELECT DepartmentId,max(Salary) as max FROM Employee GROUP BY DepartmentId)

