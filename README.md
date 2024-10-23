
# RAG Agent Using CrewAI and Groq

This project is a backend application for processing and querying PDF files using CrewAI and Groq's Retrieval-Augmented Generation (RAG) model.

## Features
- Upload PDF files and store them on the server.
- Query PDFs using CrewAI tools and Groq-powered language model to retrieve answers.
- Dockerized for easy deployment.
- Unit tests for validating API endpoints.

## Setup Instructions

### Prerequisites
- Python 3.9+
- Docker (optional for containerization)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/rag-agent-crewai-groq.git
   cd rag-agent-crewai-groq/backend
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Rename `.env.example` to `.env` and fill in your details.

### Running the App
- **Locally**:
   ```bash
   uvicorn app:app --reload
   ```
- **With Docker**:
   ```bash
   docker build -t rag-agent-crewai-groq .
   docker run -p 8000:8000 rag-agent-crewai-groq
   ```

### Testing
Run the tests using:
```bash
pytest tests/
```

### Future Work
- Further refine AI processing and model integration using advanced Groq features.
- Deploy to cloud (AWS, Heroku, etc.)
- Add frontend enhancements.
#   R A G - a g e n t - u s i n g - C r e w A i - a n d - G r o q  
 