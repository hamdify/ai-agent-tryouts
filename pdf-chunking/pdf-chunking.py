import os # dosya yollarını yönetmek
from dotenv import load_dotenv # .env dosyasından çevresel değişkenleri yüklemek
import openai # OpenAI API (ya da openrouter) ile etkileşim için
import fitz  # PyMuPDF, pdf dosyalarını okumak için


def load_pdf_chunks(pdf_path: str) -> list:
    """PDF'yi yükler ve sayfa başına metin parçalarına böler."""
    doc = fitz.open(pdf_path)
    chunks = []
    for page in doc:
        text = page.get_text().strip()
        if text:
            chunks.append(text)
    return chunks

def find_best_chunk(question: str, chunks: list) -> str:
    """Anahtar kelime örtüşmesi en fazla olan parçayı seçip LLM'e gönderir."""
    question_words = set(question.lower().split())
    best_chunk = ""
    max_matches = -1
    for chunk in chunks:
        words = set(chunk.lower().split())
        matches = len(question_words & words)
        if matches > max_matches:
            max_matches = matches
            best_chunk = chunk
    return best_chunk


def ask_llm(chunk: str, question: str) -> str:
    """Seçilen parçayı ve soruyu OpenRouter üzerinden LLM'e gönderir, cevabını alır."""
    load_dotenv()
    api_key = os.getenv("OPENROUTER_API_KEY")
    client = openai.OpenAI(api_key=api_key, base_url="https://openrouter.ai/api/v1")

    prompt = f"Belgeden Alıntı:\n{chunk}\n\nSoru: {question}\nCevap:"
    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    """Ana program akışı."""
    print("📄 PDF içeriğini sorgulama arayüzüne hoş geldiniz.\n")
    base_path = os.path.dirname(__file__)
    pdf_path = os.path.join(base_path, input("PDF dosyasının yolu nedir? (bu denemede: assets/cihad-icin-on-hadis.pdf): ").strip())


    try:
        chunks = load_pdf_chunks(pdf_path)
    except Exception as e:
        print("❌ PDF yüklenemedi:", e)
        raise SystemExit

    if not chunks:
        print("⚠️ PDF içeriği boş bulundu.")
        raise SystemExit
    
    question = input("Belgeden öğrenmek istediğiniz nedir?: ").strip()
    best_chunk = find_best_chunk(question, chunks)
    answer = ask_llm(best_chunk, question)

    print("\n📌 Cevap:\n", answer)