import os
from dotenv import load_dotenv
import openai

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

client = openai.OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)
print("\nLLM üzerinden soru yanıtlama arayüzüne hoş geldiniz.\n")
metin = input("İçinden soru soracağınız kısa bir metin girin.")
soru = input("Sormak istediğiniz soruyu girin.")

prompt = f"{metin}\nSoru: {soru}\nCevap:"

response = client.chat.completions.create(
    model="openai/gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)

print(response.choices[0].message.content)