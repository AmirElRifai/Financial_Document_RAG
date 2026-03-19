import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def load_embeddings(path):

    with open(path, "rb") as f:
        data = pickle.load(f)

    return data


def search(query, embeddings_data, top_k=5):

    query_embedding = model.encode(query)

    scores = []

    for item in embeddings_data:

        similarity = np.dot(query_embedding, item["embedding"]) / (
            np.linalg.norm(query_embedding) * np.linalg.norm(item["embedding"])
        )

        scores.append((similarity, item["text"]))

    scores.sort(reverse=True)

    results = scores[:top_k]

    return results