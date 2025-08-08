# main.py
from document_loader import load_pdf, load_docx, chunk_text
from query_engine import create_vector_store, query_vector_store, ask_llm, ask_llm_without_api, analyze_without_embeddings
import os

def run_system():
    # Check for OpenAI API key first
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY environment variable is not set!")
        print("Please set your OpenAI API key using one of these methods:")
        print("1. Export it in your terminal: export OPENAI_API_KEY='your-api-key-here'")
        print("2. Create a .env file in this directory with: OPENAI_API_KEY=your-api-key-here")
        print("3. Set it in your Python environment")
        return
    
    doc_path = "sample_policy.pdf"  # or .docx
    query = "Does this policy cover knee surgery, and what are the conditions?"

    try:
        # Step 1: Load doc
        print("📄 Loading document...")
        text = load_pdf(doc_path)  # or load_docx(doc_path)
        chunks = chunk_text(text)
        print(f"✅ Document loaded and split into {len(chunks)} chunks")

        # Step 2: Vector DB
        print("🔍 Creating vector store...")
        try:
            store = create_vector_store(chunks)
            print("✅ Vector store created")

            # Step 3: Search
            print("🔎 Searching for relevant content...")
            results = query_vector_store(store, query)
            context = "\n\n".join([doc.page_content for doc in results])
            print(f"✅ Found {len(results)} relevant chunks")

            # Step 4: Ask LLM
            print("🤖 Asking LLM...")
            try:
                answer = ask_llm(context, query)
                print("\n📋 Answer:")
                print(answer)
            except ValueError as e:
                if "quota" in str(e).lower() or "insufficient" in str(e).lower():
                    # Use fallback analysis
                    answer = ask_llm_without_api(context, query)
                    print("\n📋 Basic Analysis (API quota exceeded):")
                    print(answer)
                else:
                    print(f"❌ Error: {str(e)}")
                    
        except ValueError as e:
            if "quota" in str(e).lower() or "insufficient" in str(e).lower():
                # Use fallback analysis without embeddings
                print("⚠️  OpenAI quota exceeded during embeddings creation.")
                answer = analyze_without_embeddings(text, query)
                print("\n📋 Basic Analysis (API quota exceeded):")
                print(answer)
            else:
                print(f"❌ Error: {str(e)}")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    run_system()