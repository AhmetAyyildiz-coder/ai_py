import pyodbc
import json
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss



# 1. JSON dosyasını yükle
with open("sales_data.json", "r", encoding="utf-8") as f:
    sales_data = json.load(f)


# 2. Verileri JSON formatına dönüştür
texts = [json.dumps(record) for record in sales_data]



# 3. Modeli yükle (örneğin, SentenceTransformer)
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')  # Küçük ve hızlı bir model


# 4. Metinleri vektörlere dönüştür
text_vectors = model.encode(texts)


# 5. FAISS indeksini oluştur
dimension = text_vectors.shape[1]  # Vektör boyutu
index = faiss.IndexFlatL2(dimension)  # L2 mesafesi kullanarak indeks oluştur
index.add(text_vectors)  # Vektörleri indekse ekle


# Senaryo 5: En Çok Sipariş Veren Müşterileri Bulma
query = "En çok sipariş veren müşterileri bul."
query_vector = model.encode([query])  # Sorguyu vektöre dönüştür

k = 5  # En yakın 5 sonuç
distances, indices = index.search(query_vector, k)  # FAISS ile en yakın sonuçları bul

# Sonuçları göster
print(f"Sorgu: {query}")
for i in indices[0]:
    print(f"Bulunan Kayıt: {texts[i]}")