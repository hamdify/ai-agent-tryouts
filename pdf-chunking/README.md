# 📄 PDF Chunking – Parça Parça Okunan Belgeler

Bu klasörde, kısa PDF belgeleri (2–3 sayfa) parçalara bölünüp (chunk) analiz edilir ve LLM'e gönderilir.

## 📌 Konsept:
- PDF okunur → içerik paragraflara/sayfalara bölünür (chunking)
- Her chunk tek tek LLM'e verilir veya embedding yapılır
- Kullanıcıdan gelen soru en ilgili chunk ile birlikte kullanılır

## Amaç:
- Orta uzunluktaki belgelerde bölmeli düşünmeyi öğrenmek
- Token sınırını aşmadan belge üzerinden bilgi çıkarmak (chunk ile daha az token kullanılır)

## 🧠 Kullanılan Teknikler:
- `fitz` (PyMuPDF) ile PDF okuma
- Python list yapısı ile chunk yönetimi
- Basit keyword matching veya embedding karşılaştırması

## 🔍 Örnek Akış:
1. PDF `chunk_1`, `chunk_2`, `chunk_3` olarak ayrılır
2. Kullanıcı belgede cevabı olan bir soru sorar.
3. Tüm chunk'lar sırayla LLM'e verilir ya da en yakın chunk seçilip kullanılır
