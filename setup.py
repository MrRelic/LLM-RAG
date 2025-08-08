#!/usr/bin/env python3
"""
Setup script for LLM RAG system
"""
import os
import subprocess
import sys

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Packages installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False
    return True

def check_api_key():
    """Check if OpenAI API key is set"""
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        print("✅ OpenAI API key is set")
        return True
    else:
        print("❌ OpenAI API key is not set")
        return False

def create_env_template():
    """Create a template .env file"""
    env_content = """# OpenAI API Configuration
# Get your API key from: https://platform.openai.com/api-keys
OPENAI_API_KEY=your-api-key-here

# Optional: Set your OpenAI organization (if you have one)
# OPENAI_ORG_ID=your-org-id-here
"""
    
    if not os.path.exists(".env"):
        with open(".env", "w") as f:
            f.write(env_content)
        print("📝 Created .env template file")
        print("   Please edit .env and add your OpenAI API key")
    else:
        print("📝 .env file already exists")

def main():
    print("🚀 Setting up LLM RAG system...")
    print()
    
    # Install requirements
    if not install_requirements():
        return
    
    print()
    
    # Check API key
    if not check_api_key():
        print()
        print("🔧 To set up your API key:")
        print("1. Get your API key from: https://platform.openai.com/api-keys")
        print("2. Set it as an environment variable:")
        print("   export OPENAI_API_KEY='your-api-key-here'")
        print("3. Or create a .env file in this directory")
        create_env_template()
        print()
        print("After setting up your API key, run: python main.py")
    else:
        print()
        print("🎉 Setup complete! You can now run: python main.py")

if __name__ == "__main__":
    main()
