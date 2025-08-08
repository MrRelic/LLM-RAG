#!/usr/bin/env python3
"""
Example usage of the LLM RAG system
"""
import os
from main import run_system

def example_with_api_key():
    """Example showing how to set up and use the system"""
    
    # Method 1: Set API key programmatically (not recommended for production)
    # os.environ["OPENAI_API_KEY"] = "your-api-key-here"
    
    print("🚀 LLM RAG System Example")
    print("=" * 40)
    
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ No API key found!")
        print()
        print("To use this system, you need to:")
        print("1. Get an OpenAI API key from: https://platform.openai.com/api-keys")
        print("2. Set it as an environment variable:")
        print("   export OPENAI_API_KEY='your-api-key-here'")
        print("3. Or edit the .env file that was created by setup.py")
        print()
        print("Once you have set up your API key, run:")
        print("   python main.py")
        return
    
    # Run the system
    print("✅ API key found! Running the system...")
    print()
    run_system()

if __name__ == "__main__":
    example_with_api_key()
