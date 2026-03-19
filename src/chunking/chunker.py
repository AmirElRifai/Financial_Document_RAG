from pathlib import Path


def chunk_text(text, chunk_size=500, overlap=50):

    words = text.split()

    chunks = []

    step = chunk_size - overlap

    for i in range(0, len(words), step):

        chunk = words[i:i + chunk_size]

        chunks.append(" ".join(chunk))

    return chunks


def chunk_all_documents(input_folder, output_folder):

    Path(output_folder).mkdir(exist_ok=True)

    for file in Path(input_folder).glob("*.txt"):

        print(f"Chunking {file.name}")

        with open(file, "r") as f:
            text = f.read()

        chunks = chunk_text(text)

        output_file = Path(output_folder) / f"{file.stem}_chunks.txt"

        with open(output_file, "w") as f:
            for chunk in chunks:
                f.write(chunk + "\n\n")

    print("All documents chunked!")