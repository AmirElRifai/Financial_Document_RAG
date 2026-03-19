from src.retrieval.search import load_embeddings, search

# load embeddings
embeddings = load_embeddings("data/embeddings.pkl")

# ask a question
query = "Who are Pfizer's competitors?"

results = search(query, embeddings)

print("\nTop results:\n")

for score, text in results:

    print("Score:", score)
    print(text[:500])
    print("\n-----------------\n")