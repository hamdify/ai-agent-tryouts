"""Basit embedding (gömülü vektör) örneği.

Bu dosya, bir metnin sayısal temsilini elde etmeyi adım adım gösterir.
Artık OpenAI servisini kullanmıyoruz; metindeki harf sayımlarına dayalı
26 boyutlu bir vektör oluşturan yerel bir yöntem tercih ediyoruz.
"""

# 1) Gerekli kütüphaneler
import string
from collections import Counter


# 2) Yedek embedding fonksiyonu
def simple_embedding(text: str) -> list[int]:
    """Metindeki harf sayılarından 26 boyutlu bir vektör oluştur."""

    text = text.lower()  # harfleri küçült
    counts = Counter(ch for ch in text if ch in string.ascii_lowercase)
    return [counts.get(ch, 0) for ch in string.ascii_lowercase]


# 3) Örnek metin
metin = "Mimar Sinan İstanbul'da birçok cami tasarlamıştır."

# 4) Vektörü yerel olarak oluştur
embedding_vector = simple_embedding(metin)

# 5) Sonuçları göster
print(f"Vektör boyutu: {len(embedding_vector)}")
print("İlk 5 değer:", embedding_vector[:5])
