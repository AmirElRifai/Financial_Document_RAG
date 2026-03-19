from pathlib import Path
from sentence_transformers import SentenceTransformer
import pickle

model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_chunks(input_folder, output_file):

    embeddings_data = []

    for file in Path(input_folder).glob("*_chunks.txt"):

        print(f"Embedding {file.name}")

        with open(file, "r") as f:
            chunks = f.read().split("\n\n")

        for chunk in chunks:

            if chunk.strip() == "":
                continue

            vector = model.encode(chunk)

            embeddings_data.append({
                "text": chunk,
                "embedding": vector
            })

    with open(output_file, "wb") as f:
        pickle.dump(embeddings_data, f)

    print("All embeddings created and saved!")