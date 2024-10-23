from crewai_tools import PDFSearchTool
from langchain_openai import ChatOpenAI
import os

# Initialize the language model with Groq API
llm = ChatOpenAI(
    api_key=os.getenv('GROQ_API_KEY'),
    model="llama3-8b-8192",
    model_kwargs={"api_base": os.getenv('API_BASE_URL')}
)

def process_pdf(question, filename):
    # Construct the path to the PDF file in the uploads directory
    pdf_path = f"uploads/{filename}"

    # Use CrewAI’s PDFSearchTool for PDF handling
    pdf_tool = PDFSearchTool(pdf=pdf_path, config=dict(
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

    # Retrieve the response based on the provided question
    response = pdf_tool.retrieve_response(question)
    return response
