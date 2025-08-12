#  Multi-Doc RAG – Çoklu Belgelerden Akıllı Cevaplama

(henüz geliştirilemedi...)

Bu klasörde, uzun metinler (>10 sayfa) veya birden fazla belgeyi işleyerek RAG (Retrieval-Augmented Generation) mimarisiyle akıllı cevaplama yapıyoruz.

## Konsept:
- Çoklu metin veya uzun PDF dosyaları chunk'lara bölünür
- Her chunk `embedding` ile vektör formatına dönüştürülür
- Kullanıcıdan gelen soru embed edilir ve vektör veritabanında en benzer parça seçilir
- Seçilen içerik + soru birlikte LLM'e gönderilerek cevap üretilir

## Amaç:
- Gerçek dünya belgelerinden akıllı bilgi çıkarımı
- RAG yapısının uçtan uca uygulanması
- Belge tabanlı agent sistemlerinin temelini kurmak

## Kullanılan Teknolojiler:
- ChromaDB (vector database)
- OpenRouter Embedding API
- `text-embedding-ada-002`
- PDF & metin parsing, chunking, filtering

## Örnek Uygulama:
- Belgeler: `project_summary.pdf`, `team_report.md`, `faq.txt`
- Soru: “Şirketin 2024 sürdürülebilirlik hedefleri nelerdir?”
- Cevap: En uygun chunk bulunur → LLM'e bağlam verilir → akıllı yanıt döner