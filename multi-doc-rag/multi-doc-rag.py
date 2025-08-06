import os
from pathlib import Path
from typing import List
import openai
import chromadb
import fitz  # PyMuPDF
from dotenv import load_dotenv


def load_document(path: str) -> str:
    """Belgeyi (PDF, MD, TXT) okuyup düz metin döndürür."""
    ext = Path(path).suffix.lower()
    if ext == ".pdf":
        doc = fitz.open(path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    else:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()


def chunk_text(text: str, size: int = 800, overlap: int = 200) -> List[str]:
    """Metni üst üste binmeli parçalara böler."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks


def get_embedding(client: openai.OpenAI, text: str, model: str = "text-embedding-ada-002") -> List[float]:
    """OpenRouter embedding API ile metni vektöre dönüştürür."""
    response = client.embeddings.create(model=model, input=text)
    return response.data[0].embedding


def build_vector_store(files: List[str], client: openai.OpenAI) -> chromadb.Collection:
    """Belge parçalarını vektör veritabanına yükler."""
    chroma_client = chromadb.Client()
    collection = chroma_client.create_collection(name="docs")
    for file in files:
        text = load_document(file)
        chunks = chunk_text(text)
        for idx, chunk in enumerate(chunks):
            emb = get_embedding(client, chunk)
            collection.add(
                documents=[chunk],
                embeddings=[emb],
                metadatas=[{"source": Path(file).name}],
                ids=[f"{Path(file).stem}-{idx}"]
            )
    return collection


def answer_question(question: str, collection: chromadb.Collection, client: openai.OpenAI) -> str:
    """Soruya en yakın chunk'ı bulup LLM'e gönderir."""
    q_emb = get_embedding(client, question)
    results = collection.query(query_embeddings=[q_emb], n_results=1)
    context = results["documents"][0][0]
    prompt = (
        "Aşağıdaki bilgilere dayanarak soruyu cevapla.\n\n"
        f"{context}\n\nSoru: {question}\nCevap:"
    )
    completion = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    return completion.choices[0].message.content.strip()


def main() -> None:
    """Örnek kullanım akışı."""
    load_dotenv()
    api_key = os.getenv("OPENROUTER_API_KEY")
    client = openai.OpenAI(api_key=api_key, base_url="https://openrouter.ai/api/v1")

    base = Path(__file__).parent
    docs = [
        base / "project_summary.pdf",
        base / "team_report.md",
        base / "faq.txt",
    ]

    collection = build_vector_store([str(p) for p in docs], client)
    soru = input("Sorunuz nedir?: ")
    cevap = answer_question(soru, collection, client)
    print("\n📌 Cevap:\n", cevap)


if __name__ == "__main__":
    main()