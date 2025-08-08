#!/usr/bin/env python3
"""
Test different queries on the policy document
"""
import os
from main import run_system
from document_loader import load_pdf, chunk_text
from query_engine import analyze_without_embeddings

def test_different_queries():
    """Test various queries on the policy"""
    
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Please set your OpenAI API key first!")
        return
    
    # Load the document once
    print("📄 Loading document...")
    text = load_pdf("sample_policy.pdf")
    print("✅ Document loaded")
    
    # Test different queries
    queries = [
        "Does this policy cover knee surgery, and what are the conditions?",
        "What medical procedures are covered under this policy?",
        "Are there any exclusions or limitations mentioned?",
        "What is the coverage amount for surgical procedures?",
        "Does this policy cover pre-existing conditions?"
    ]
    
    print("\n" + "="*60)
    print("🔍 TESTING DIFFERENT QUERIES")
    print("="*60)
    
    for i, query in enumerate(queries, 1):
        print(f"\n📋 Query {i}: {query}")
        print("-" * 50)
        
        try:
            answer = analyze_without_embeddings(text, query)
            print(answer)
        except Exception as e:
            print(f"❌ Error: {str(e)}")
        
        print("\n" + "="*60)

if __name__ == "__main__":
    test_different_queries()
