Example 1 
```
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
```



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

Senaryo 1: Belirli Bir Müşterinin Tüm Siparişlerini Getirme 
```
SELECT * 
FROM ExtendedSalesOrderSummary
WHERE CustomerID = 12345;  -- Örnek müşteri ID'si


-- py kodu
# Senaryo 1: Belirli bir müşterinin tüm siparişlerini getir
customer_id = 12345  # Örnek müşteri ID'si
cursor.execute(f"SELECT * FROM ExtendedSalesOrderSummary WHERE CustomerID = {customer_id}")
rows = cursor.fetchall()

# Verileri JSON formatına dönüştür
customer_orders = []
for row in rows:
    customer_orders.append({
        "SalesOrderID": row.SalesOrderID,
        "OrderDate": str(row.OrderDate),
        "CustomerID": row.CustomerID,
        "FirstName": row.FirstName,
        "LastName": row.LastName,
        "ProductID": row.ProductID,
        "ProductName": row.ProductName,
        "OrderQty": row.OrderQty,
        "UnitPrice": float(row.UnitPrice),
        "LineTotal": float(row.LineTotal),
        "OrderStatus": row.OrderStatus
    })

# JSON'u dosyaya kaydet (opsiyonel)
with open("customer_orders.json", "w") as f:
    json.dump(customer_orders, f, indent=4)

print(f"Müşteri ID {customer_id} için siparişler: {json.dumps(customer_orders, indent=4)}")
```
