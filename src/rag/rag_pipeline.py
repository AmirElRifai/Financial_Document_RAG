import os
from src.retrieval.search import load_embeddings, search
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def ask_rag(query):

    embeddings = load_embeddings("data/embeddings.pkl")

    results = search(query, embeddings, top_k=5)

    context = ""

    for score, text in results:
        context += text + "\n\n"

    prompt = f"""
Use the context below to answer the question.

Context:
{context}

Question:
{query}

Answer clearly using the information above.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content