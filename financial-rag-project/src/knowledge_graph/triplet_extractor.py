import os
from openai import OpenAI
from src.retrieval.search import load_embeddings

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def extract_triplets(text):

    prompt = f"""
Extract relationships from the text below.

Return results as triplets in the format:

(Entity1, RELATION, Entity2)

Example:
(Pfizer, COMPETES_WITH, Moderna)

Text:
{text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content