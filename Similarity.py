"""Basit benzerlik ornegi.

Bu skript, iki metin arasindaki benzerligi hesaplamak icin
simple_embedding fonksiyonunu kullanir. Hesaplama kosinus
benzerligine dayanir.
"""

import math
import string
from collections import Counter


def simple_embedding(text: str) -> list[int]:
    """Metindeki harf sayilarindan 26 boyutlu bir vektor olustur."""
    text = text.lower()
    counts = Counter(ch for ch in text if ch in string.ascii_lowercase)
    return [counts.get(ch, 0) for ch in string.ascii_lowercase]


def cosine_similarity(v1, v2):
    dot = sum(a * b for a, b in zip(v1, v2))
    norm1 = math.sqrt(sum(a * a for a in v1))
    norm2 = math.sqrt(sum(b * b for b in v2))
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot / (norm1 * norm2)


# Ornek metinler
text1 = "Mimar Sinan Istanbul'da bircok cami tasarlamistir."
text2 = "Sinan'in Istanbul'da insa ettigi eserler oldukca fazladir."

# Vektorleri olustur
vec1 = simple_embedding(text1)
vec2 = simple_embedding(text2)

# Benzerligi hesapla
similarity = cosine_similarity(vec1, vec2)

print(f"Benzerlik skoru: {similarity:.4f}")
