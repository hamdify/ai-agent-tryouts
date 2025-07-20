import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

client = openai.OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

# Embedding alınacak metin
metin = "Mimar Sinan İstanbul'da birçok cami tasarlamıştır."

# OpenAI GPT-3.5 modeline göre vektör üret
embedding_response = client.embeddings.create(
    model="openai/text-embedding-ada-002",
    input=metin
)

embedding_vector = embedding_response.data[0].embedding
print(f"Vektör boyutu: {len(embedding_vector)}")
print("İlk 5 değer:", embedding_vector[:5])
