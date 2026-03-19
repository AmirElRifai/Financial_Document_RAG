from src.rag.rag_pipeline import ask_rag
from src.retrieval.search import load_embeddings, search
from src.evaluation.llm_judge import judge_answer

query = "Who are Pfizer's competitors?"

embeddings = load_embeddings("data/embeddings.pkl")

results = search(query, embeddings)

context = ""
for score, text in results:
    context += text + "\n\n"

answer = ask_rag(query)

evaluation = judge_answer(query, context, answer)

print("\nQUESTION:\n", query)
print("\nANSWER:\n", answer)
print("\nEVALUATION:\n", evaluation)