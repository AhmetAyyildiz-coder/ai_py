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
----------------------------
Senaryo 1: Belirli Bir Müşterinin Tüm Siparişlerini Getirme 
```
# TSQL ile senaryo 1 nasıl yapılır?
SELECT * 
FROM ExtendedSalesOrderSummary
WHERE CustomerID = 12345;  -- Örnek müşteri ID'si

# AI kullanarak senaryo 1 nasıl yapılır?
query = "Müşteri ID 12345'in tüm siparişlerini getir."
# Doğal dil sorgusunu vektöre dönüştür
query_vector = model.encode([query])

# FAISS ile en yakın sonuçları bul
k = 5  # En yakın 5 sonuç
distances, indices = index.search(query_vector, k)

# Sonuçları göster
for i in indices[0]:
    print(f"Bulunan Kayıt: {texts[i]}")

```
-----------------------------

Senaryo 2: Belirli Bir Tarih Aralığındaki Siparişleri Getirme

```

# senaryo 2 : TSQL ile nasıl yazılır?
SELECT * 
FROM ExtendedSalesOrderSummary
WHERE OrderDate BETWEEN '2013-01-01' AND '2013-12-31';  -- Örnek tarih aralığı


# senaryo 2 : AI anlayacağı şekilde nasıl yazılır?
query = "2013 yılında yapılan siparişleri getir."


```
---------------

## Senaryo 3 : En Yüksek Toplam Tutara Sahip Siparişleri Getirme

```
# senaryo 3 : TSQL ile senaryo 3 nasıl yazılır?
SELECT TOP 10 * 
FROM ExtendedSalesOrderSummary
ORDER BY LineTotal DESC;


# senaryo 3 : AI ile nasıl sorgulanır?
query = "En yüksek tutarlı siparişleri getir."

```

---------------------------------------------
## Senaryo 4: Belirli Bir Ürünün Satış Bilgilerini Getirme

```

# TSQL
SELECT * 
FROM ExtendedSalesOrderSummary
WHERE ProductID = 707;  -- Örnek ürün ID'si

# AI
query = "Ürün ID 707'nin satış bilgilerini getir."


```
------------------------------------------------------------

## Senaryo 6: En Çok Sipariş Veren Müşterileri Bulma
```
# TSQL 
SELECT TOP 5 CustomerID, FirstName, LastName, COUNT(*) AS OrderCount
FROM ExtendedSalesOrderSummary
GROUP BY CustomerID, FirstName, LastName
ORDER BY OrderCount DESC;

# AI
query = "En çok sipariş veren müşterileri bul."

```
