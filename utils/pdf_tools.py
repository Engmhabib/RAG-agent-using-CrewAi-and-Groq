
from crewai_tools import PDFSearchTool
from langchain_openai import ChatOpenAI
import os

# Initialize the language model with Groq API
llm = ChatOpenAI(
    api_key=os.getenv('GROQ_API_KEY'),
    model="llama3-8b-8192",
    model_kwargs={"api_base": "https://api.groq.com/openai/v1"}
)

def process_pdf(question, filename):
    # Use CrewAI’s PDFSearchTool for PDF handling
    pdf_tool = PDFSearchTool(pdf=f"backend/{filename}", config=dict(
        llm=dict(
            provider="groq",
            config=dict(
                model="llama3-8b-8192"
            ),
        ),
        embedder=dict(
            provider="huggingface",
            config=dict(
                model="BAAI/bge-small-en-v1.5"
            ),
        ),
    ))
    
    response = pdf_tool.retrieve_response(question)
    return response
