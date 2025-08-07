# query_engine.py
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document
import openai

def create_vector_store(chunks):
    docs = [Document(page_content=chunk) for chunk in chunks]
    embeddings = OpenAIEmbeddings()
    return FAISS.from_documents(docs, embeddings)

def query_vector_store(store, query):
    return store.similarity_search(query, k=3)

def ask_llm(context, query):
    prompt = f"""
You are a policy analyzer. Read the clauses below:

{context}

Question: "{query}"

Return a JSON:
{{
  "answer": "...",
  "conditions": [...],
  "source_clauses": ["..."],
  "rationale": "..."
}}
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response['choices'][0]['message']['content']