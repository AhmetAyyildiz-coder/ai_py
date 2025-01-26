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
