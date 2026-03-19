from src.knowledge_graph.triplet_extractor import extract_triplets
from src.retrieval.search import load_embeddings

embeddings = load_embeddings("data/embeddings.pkl")

sample_text = embeddings[0]["text"]

triplets = extract_triplets(sample_text)

print("\nExtracted Knowledge:\n")
print(triplets)