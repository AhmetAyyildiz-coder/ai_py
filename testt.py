import pyodbc
import json
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

# SQL Server Connection using your provided connection string
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=AHMET_123;"
    "DATABASE=AdventureWorks2017;"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()

# View'den verileri çek
cursor.execute("SELECT top 100 * FROM SalesOrderSummary")
rows = cursor.fetchall()

# Verileri JSON formatına dönüştür
data = []
for row in rows:
    data.append({
        "SalesOrderID": row.SalesOrderID,
        "OrderDate": str(row.OrderDate),
        "CustomerID": row.CustomerID,
        "ProductID": row.ProductID,
        "OrderQty": row.OrderQty,
        "UnitPrice": float(row.UnitPrice),
        "LineTotal": float(row.LineTotal)
    })

# JSON'u dosyaya kaydet (opsiyonel)
with open("sales_data.json", "w") as f:
    json.dump(data, f, indent=4)

# Embedding Modelini Yükle
model = SentenceTransformer('all-MiniLM-L6-v2')

# Verileri Vektörlere Dönüştür
texts = [json.dumps(record) for record in data]  # JSON'u metin olarak kullan
vectors = model.encode(texts)

# FAISS ile Vektör Veritabanı Oluştur
dimension = vectors.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(vectors))

# Örnek Sorgu
query = "Sipariş ID 43659 ile ilgili bilgileri getir."
query_vector = model.encode([query])
k = 3  # En yakın 3 sonucu bul
distances, indices = index.search(query_vector, k)

# Sonuçları Göster
for i in indices[0]:
    print(f"Bulunan Kayıt: {texts[i]}")