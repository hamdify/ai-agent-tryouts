# AI Agent Tryouts – Practice Repository

Bu repoda, Large Language Model (LLM) temelli uygulamalar için yaptığım deneysel alıştırmaları bulacaksınız. Her klasör, metin işleme derinliği göre düzenlendi. Promptlama, embedding, chunking ve RAG mimarilerine dair adım adım gelişen örnekleri içerir.

## Klasör Yapısı

### 1. `simple-prompting `
- Küçük bir metin ve ona bağlı soru tek bir prompt içinde LLM'e verilir.
- RAG veya embedding yapılmaz.

- Hedef: LLM'in doğrudan anlama ve cevaplama becerisini test etmek.

### 2. `pdf-chunking`
- 2–3 sayfalık PDF dosyası sayfalara/paragraflara bölünür (chunking).
- Her chunk embedding'e çevrilir.
- Kullanıcıdan gelen soru, uygun chunk ile birlikte LLM'e gönderilir.

- Hedef: Küçük belgelerde manuel chunk + context aware prompting.

### 3. `multi-doc-rag`
- 10+ sayfalık veya çoklu belge içeriği embedding ile vektör veritabanına alınır.
- Kullanıcı sorusu embed edilir ve vektör benzerliğine göre en uygun içerik çekilir.
- Bu içerik + soru birlikte LLM'e verilir (RAG: Retrieval-Augmented Generation).

- Hedef: RAG mimarisini uçtan uca kurmak.

---

Her alt klasör, kendine ait bir README içerir.

---

## Kullanılan Teknolojiler
- Python
- OpenAI / OpenRouter API
- FAISS (vector similarity)
- Python-dotenv
- PDF parsing (PyMuPDF, pdfminer)
- Streamlit (bazı UI denemeleri için)

---

## 📌 Katkı
Bu repo kişisel öğrenme ve deneme amaçlıdır.

---
