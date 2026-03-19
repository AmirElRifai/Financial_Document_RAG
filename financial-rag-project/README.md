Financial RAG Project
Retrieval-Augmented Generation and Knowledge Extraction from Corporate Filings
Course: Natural Language Processing
Program: MSc AI for Business Transformation – SKEMA Business School
Authors: Amir El Rifai, Yvonne Khayata
Year: 2026

1. Project Overview
This project explores how Natural Language Processing (NLP) and Large Language Models (LLMs) can be used to analyze corporate financial filings.
We designed a system capable of:
• indexing large financial reports
• answering natural language questions about company filings
• extracting structured knowledge from financial documents
• evaluating answer quality using an LLM-based evaluation framework
The system implements a Retrieval-Augmented Generation (RAG) architecture combined with knowledge graph extraction techniques.
The goal is to transform unstructured financial reports (SEC 10-K and 10-Q filings) into a searchable and analyzable knowledge base.

2. Dataset
The dataset consists of publicly available SEC financial filings from multiple companies across different industries.
Companies included:
• 3M
• Adobe
• Amazon
• AMD
• Boeing
• Lockheed Martin
• Pfizer
• Activision Blizzard
Document types:
• 10-K annual reports
• 10-Q quarterly reports
These reports contain detailed information about:
• company operations
• competitive landscape
• financial performance
• risk factors
• strategic initiatives
Because each report can exceed 100 pages, traditional search techniques are insufficient, making them ideal for NLP analysis.

3. System Architecture
The project implements a multi-stage NLP pipeline.
Financial PDFs
       ↓
PDF Text Extraction
       ↓
Document Chunking
       ↓
Embedding Generation
       ↓
Vector Similarity Search
       ↓
Context Retrieval
       ↓
LLM Reasoning (RAG)
       ↓
Final Answer
Additionally, a knowledge extraction module generates structured relationships between entities.
Financial Text
       ↓
LLM Information Extraction
       ↓
(Entity, Relation, Entity) Triplets
       ↓
Knowledge Graph

4. Data Processing Pipeline
PDF Parsing
Financial filings are first converted from PDF format into raw text using the pdfplumber library.
This step extracts textual content from all pages of the filings.
Document Chunking
Since LLMs cannot process extremely long documents, each report is divided into smaller text segments called chunks.
Chunk configuration:
• Chunk size: 500 tokens
• Overlap: 50 tokens
Chunking ensures that:
• contextual information is preserved
• retrieval accuracy is improved

5. Embedding Generation
Each text chunk is converted into a numerical vector using the Sentence Transformers model:
all-MiniLM-L6-v2
This model maps sentences into high-dimensional vector space where semantically similar text is located close together.
Example:
"The Boeing Company is a major aerospace manufacturer"
→ vector representation
[0.231, -0.492, 0.773, ...]
Embeddings allow the system to perform semantic search instead of keyword matching.

6. Vector Search
All embeddings are stored in a searchable structure.
When a user asks a question:
The question is converted into an embedding
Similar chunks are retrieved using cosine similarity
The most relevant chunks are returned as context
Example query:
Who are Pfizer's competitors?
The system retrieves relevant paragraphs from Pfizer’s filings discussing competition.

7. Retrieval-Augmented Generation (RAG)
The retrieved context is passed to a Large Language Model (GPT-4o-mini) along with the user’s question.
The model then generates a final answer grounded in the retrieved documents.
Example output:
Pfizer faces competition from several pharmaceutical companies
including Johnson & Johnson, Merck, Novartis, and other biotechnology firms.
RAG significantly improves answer accuracy because the model reasons over actual document content.

8. Knowledge Extraction
Beyond question answering, the system extracts structured knowledge from financial reports.
The LLM identifies relationships between entities and returns them as triplets.
Example output:
(Pfizer, COMPETES_WITH, Moderna)
(Boeing, COMPETES_WITH, Airbus)
(Amazon, ACQUIRED, Whole Foods)
These triplets can be used to build knowledge graphs of corporate relationships.
Example output from our system:
(LOCKHEED MARTIN CORPORATION, HAS_TRADING_SYMBOL, LMT)
(LOCKHEED MARTIN CORPORATION, REGISTERED_ON, New York Stock Exchange)

9. Evaluation — LLM as a Judge
To evaluate answer quality, we implemented an LLM-as-a-Judge evaluation framework.
The evaluation model receives:
• the original question
• retrieved context
• the generated answer
It then determines whether the answer is supported by the context.
Example:
Evaluation: CORRECT
The answer accurately reflects information present in the retrieved context.
This evaluation method is increasingly used in modern AI research.

10. Experimental Results
Pipeline execution time (MacBook Pro):
~1 minute
Performance observations:
• semantic retrieval returned relevant chunks consistently
• RAG produced coherent and context-grounded answers
• knowledge extraction successfully identified structured relationships

11. Limitations
Several limitations remain:
• small dataset size compared to enterprise document collections
• knowledge extraction depends on LLM interpretation
• financial filings sometimes contain highly technical language
• competitor information is not always explicitly listed in filings
Future work could include:
• using larger embedding models
• building a full knowledge graph database
• integrating financial market datasets

12. Technologies Used
Python
Sentence Transformers
OpenAI GPT-4o-mini
pdfplumber
NumPy
pickle

13. Repository Structure
financial-rag-project

data/
    raw_pdfs/
    processed_text/
    chunks/
    embeddings.pkl

src/
    chunking/
    embeddings/
    evaluation/
    knowledge_graph/
    pdf_processing/
    rag/
    retrieval/

run_pipeline.py
ask_rag.py
extract_knowledge.py
evaluate_rag.py
requirements.txt
README.md

14. Conclusion
This project demonstrates how modern NLP techniques can transform unstructured financial filings into an intelligent knowledge system.
By combining:
• semantic search
• retrieval-augmented generation
• knowledge extraction
• LLM-based evaluation
We created a pipeline capable of analyzing corporate filings in a scalable and interpretable way.
Such systems could be extended to build AI-powered financial research assistants capable of analyzing thousands of corporate reports.