import openai
import os
from dotenv import load_dotenv
import faiss
import numpy as np

# .env dosyasını yükle
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

# OpenRouter GPT istemcisi
client = openai.OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

# ▶️ 1. Embedding alınacak metin
metin = "Hamdi Çakır, 2025 yılında One Click LCA firmasında iş analisti olarak görev almıştır. Görevi, yazılım kalitesini artırmak için generative design algoritmalarının entegrasyon sürecine destek olmaktı."

# ▶️ 2. Bu metni embed et
embedding_response = client.embeddings.create(
    model="openai/text-embedding-ada-002",
    input=metin
)
embedding_vector = embedding_response.data[0].embedding

# ▶️ 3. FAISS index oluştur ve vektörü ekle
embedding_np = np.array([embedding_vector]).astype("float32")
index = faiss.IndexFlatL2(1536)
index.add(embedding_np)

# ▶️ 4. Kullanıcıdan soru al
soru = input("Soru gir: ")

# ▶️ 5. Soru için embedding oluştur
soru_vec = client.embeddings.create(
    model="openai/text-embedding-ada-002",
    input=soru
).data[0].embedding
soru_np = np.array([soru_vec]).astype("float32")

# ▶️ 6. FAISS ile benzerlik araması yap
mesafe, sonuc = index.search(soru_np, k=1)
print("\n📌 En yakın içerik ID:", sonuc[0][0])
print("🔍 Mesafe:", mesafe[0][0])
print("\n📄 Cevap olabilecek içerik:\n", metin)
