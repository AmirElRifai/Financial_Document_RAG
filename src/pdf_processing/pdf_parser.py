import pdfplumber
from pathlib import Path

def extract_text_from_pdf(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def parse_all_pdfs(input_folder, output_folder):

    Path(output_folder).mkdir(exist_ok=True)

    for pdf in Path(input_folder).glob("*.pdf"):

        print(f"Parsing {pdf.name}")

        text = extract_text_from_pdf(pdf)

        output_file = Path(output_folder) / (pdf.stem + ".txt")

        with open(output_file, "w") as f:
            f.write(text)

    print("All PDFs parsed successfully!")