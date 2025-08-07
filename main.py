# main.py
from document_loader import load_pdf, load_docx, chunk_text
from query_engine import create_vector_store, query_vector_store, ask_llm

def run_system():
    doc_path = "sample_policy.pdf"  # or .docx
    query = "Does this policy cover knee surgery, and what are the conditions?"

    # Step 1: Load doc
    text = load_pdf(doc_path)  # or load_docx(doc_path)
    chunks = chunk_text(text)

    # Step 2: Vector DB
    store = create_vector_store(chunks)

    # Step 3: Search
    results = query_vector_store(store, query)
    context = "\n\n".join([doc.page_content for doc in results])

    # Step 4: Ask LLM
    answer = ask_llm(context, query)
    print(answer)

if __name__ == "__main__":
    run_system()