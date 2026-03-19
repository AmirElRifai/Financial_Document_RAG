from src.rag.rag_pipeline import ask_rag

query = "Who are Pfizer's competitors?"

answer = ask_rag(query)

print("\nAI Answer:\n")
print(answer)