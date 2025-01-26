Example 1 
``
CREATE VIEW SalesOrderSummary AS
SELECT 
    SOH.SalesOrderID,
    SOH.OrderDate,
    SOH.CustomerID,
    SOD.ProductID,
    SOD.OrderQty,
    SOD.UnitPrice,
    SOD.LineTotal
FROM 
    Sales.SalesOrderHeader SOH
JOIN 
    Sales.SalesOrderDetail SOD ON SOH.SalesOrderID = SOD.SalesOrderID;
``



Example 2 

```
CREATE VIEW ExtendedSalesOrderSummary AS
SELECT 
    soh.SalesOrderID,
    soh.OrderDate,
    soh.CustomerID,
    p.FirstName,
    p.LastName,
    sod.ProductID,
    pr.Name AS ProductName,
    sod.OrderQty,
    sod.UnitPrice,
    sod.LineTotal,
    soh.Status AS OrderStatus
FROM 
    Sales.SalesOrderHeader soh
JOIN 
    Sales.SalesOrderDetail sod ON soh.SalesOrderID = sod.SalesOrderID
JOIN 
    Sales.Customer c ON soh.CustomerID = c.CustomerID
JOIN 
    Person.Person p ON c.PersonID = p.BusinessEntityID  -- Müşteri bilgileri için Person tablosuna JOIN
JOIN 
    Production.Product pr ON sod.ProductID = pr.ProductID;

```
