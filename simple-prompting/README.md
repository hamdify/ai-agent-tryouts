# Simple Prompting – Text & Question in One Prompt

Bu klasörde, çok küçük bilgi metinleriyle (1–2 cümle) doğrudan LLM'e sorular sorduğumuz örnekler yer alır.

## Konsept:
- Her şey **tek prompt** içinde yapılır.
- Embedding, chunking veya vektör veritabanı yoktur.
- Sadece `text + question` → prompt → `LLM response` zinciri kullanılır.

## Örnek Kullanım:
```python
metin = "Hamdi Çakır, 1 Temmuz 2025'te Cuswa Tech'de Business Development Executive olarak çalışmaya başladı." 
soru = "Hamdi ne zaman Cuswa Tech'de çalışmaya başladı?"
```
Bu ikisi prompt içinde birleştirilir ve LLM'e gönderilir.

## Not:
Bu yöntem küçük metinlerde uygundur. Daha uzun belgelerde chunking gerekir.
