from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import os
import logging
from utils.pdf_tools import process_pdf  # The utility function configured for CrewAI and Groq

# Load environment variables
load_dotenv()

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Serve static files (HTML, CSS, JS)
app.mount("/", StaticFiles(directory="static", html=True), name="static")

# Ensure the uploads directory exists
uploads_directory = "uploads"
os.makedirs(uploads_directory, exist_ok=True)

# Endpoint to upload a PDF
@app.post("/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        file_location = f"{uploads_directory}/{file.filename}"
        with open(file_location, "wb") as f:
            f.write(await file.read())
        logger.info(f"PDF uploaded successfully: {file_location}")
        return {"message": "PDF uploaded successfully", "filename": file.filename}
    except Exception as e:
        logger.error(f"Error uploading PDF: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to upload PDF")

# Endpoint to query the uploaded PDF using CrewAI and Groq
@app.post("/query_pdf")
async def query_pdf(question: str, filename: str):
    try:
        response = process_pdf(question, filename)  # Function defined in utils/pdf_tools.py
        logger.info(f"Response generated: {response}")
        return JSONResponse(content={"answer": response})
    except Exception as e:
        logger.error(f"Error while processing query: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to process the query")
