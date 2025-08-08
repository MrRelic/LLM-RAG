# LLM Query Retrieval System

A RAG (Retrieval-Augmented Generation) system that can analyze policy documents and answer questions about them using OpenAI's GPT models.

## Features

- 📄 Load PDF and DOCX documents
- 🔍 Create vector embeddings for semantic search
- 🤖 Query documents using natural language
- 📋 Get structured answers with conditions and rationale

## Quick Start

### 1. Setup Environment

```bash
# Install dependencies
python setup.py

# Or manually install
pip install -r requirements.txt
```

### 2. Configure OpenAI API Key

You need an OpenAI API key to use this system. Get one from [OpenAI Platform](https://platform.openai.com/api-keys).

**Option A: Environment Variable**
```bash
export OPENAI_API_KEY='your-api-key-here'
```

**Option B: .env File**
Create a `.env` file in the project directory:
```
OPENAI_API_KEY=your-api-key-here
```

### 3. Run the System

```bash
python main.py
```

## How It Works

1. **Document Loading**: The system loads your PDF/DOCX document
2. **Text Chunking**: Breaks the document into smaller chunks for processing
3. **Vector Embedding**: Creates embeddings for semantic search
4. **Query Processing**: Searches for relevant content based on your question
5. **LLM Response**: Uses GPT to generate a structured answer

## File Structure

- `main.py` - Main execution script
- `document_loader.py` - PDF/DOCX loading and text processing
- `query_engine.py` - Vector store and LLM integration
- `setup.py` - Environment setup script
- `sample_policy.pdf` - Example document for testing

## Troubleshooting

### Common Issues

1. **"OPENAI_API_KEY environment variable is required"**
   - Set your OpenAI API key as shown in the setup section

2. **Import errors with LangChain**
   - Run `pip install -r requirements.txt` to install the latest packages

3. **PDF loading errors**
   - Ensure PyMuPDF is installed: `pip install PyMuPDF`

### Dependencies

- `openai` - OpenAI API client
- `langchain` - LangChain framework
- `langchain-community` - Community LangChain components
- `langchain-openai` - OpenAI LangChain integrations
- `faiss-cpu` - Vector similarity search
- `PyMuPDF` - PDF processing
- `python-docx` - DOCX processing
- `tiktoken` - Token counting

## Customization

### Adding Your Own Documents

Replace `sample_policy.pdf` with your own document in `main.py`:

```python
doc_path = "your_document.pdf"  # or .docx
```

### Modifying Queries

Change the query in `main.py`:

```python
query = "Your question about the document here?"
```

### Adjusting Chunk Size

Modify the chunk size in `document_loader.py`:

```python
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
```

## License

This project is for educational purposes. Please ensure you comply with OpenAI's terms of service when using their API.
