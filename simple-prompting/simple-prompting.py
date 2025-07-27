import os
from dotenv import load_dotenv
import openai

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

client = openai.OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

metin = "Hamdi Çakır, 1 Temmuz 2025'te Cuswa Tech'de Business Development Executive olarak çalışmaya başladı. Bugünün tarihi ise 27-07-2025." 
soru = "Hamdi kaç günür Cuswa Tech'de çalışıyor?"

prompt = f"{metin}\nSoru: {soru}\nCevap:"

response = client.chat.completions.create(
    model="openai/gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)

print(response.choices[0].message.content)