-- https://leetcode.com/problems/customers-who-never-order/

-- Suppose that a website contains two tables, the Customers table and 
-- the Orders table. Write a SQL query to find all customers who never order anything.

-- Table: Customers.

-- +----+-------+
-- | Id | Name  |
-- +----+-------+
-- | 1  | Joe   |
-- | 2  | Henry |
-- | 3  | Sam   |
-- | 4  | Max   |
-- +----+-------+
-- Table: Orders.

-- +----+------------+
-- | Id | CustomerId |
-- +----+------------+
-- | 1  | 3          |
-- | 2  | 1          |
-- +----+------------+
-- Using the above tables as example, return the following:

-- +-----------+
-- | Customers |
-- +-----------+
-- | Henry     |
-- | Max       |
-- +-----------+



SELECT Name as Customers
FROM Customers
WHERE Id Not in (SELECT Distinct(CustomerId) FROM Orders)



-- select c.Name from Customers c
-- where c.Id not in (select customerId from Orders)

-- select c.Name from Customers c
-- where (select count(*) from Orders o where o.customerId=c.id)=0

-- select c.Name from Customers c
-- where not exists (select * from Orders o where o.customerId=c.id)

