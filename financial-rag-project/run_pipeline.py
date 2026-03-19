from src.pdf_processing.pdf_parser import parse_all_pdfs
from src.chunking.chunker import chunk_all_documents
from src.embeddings.embedder import embed_chunks

# Step 1
parse_all_pdfs(
    "data/raw_pdfs",
    "data/processed_text"
)

# Step 2
chunk_all_documents(
    "data/processed_text",
    "data/chunks"
)

# Step 3
embed_chunks(
    "data/chunks",
    "data/embeddings.pkl"
)