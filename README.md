# RAG Agent using CrewAI and Groq

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95.2-green)
![Docker](https://img.shields.io/badge/Docker-Supported-blue)
![GitHub](https://img.shields.io/github/license/Engmhabib/RAG-agent-using-CrewAi-and-Groq)

This project demonstrates a Retrieval-Augmented Generation (RAG) agent that leverages **CrewAI** and **Groq** technologies to process and query PDF files. The backend application is built with **FastAPI** and provides endpoints for uploading and querying PDFs. It is designed for easy deployment and integration with modern AI services.

## Features

- **PDF Upload**: Upload PDF files directly to the server for processing.
- **Query PDFs**: Ask questions about the content of uploaded PDFs using a Groq-powered language model.
- **CrewAI Integration**: Utilizes CrewAI tools to extract and interpret data from PDF files efficiently.
- **Groq-Powered AI Model**: Integrates with Groq's API for advanced language model processing.
- **Dockerized Deployment**: Easily deployable using Docker for consistent runtime environments.
- **Unit Tests**: Basic unit tests for API endpoint validation using `pytest`.

## Technologies Used

- **FastAPI**: A modern, fast (high-performance) web framework for Python.
- **CrewAI**: Tools for efficient PDF processing and data extraction.
- **Groq**: Integration with Groq’s API for advanced language model processing.
- **Docker**: Containerized deployment for easy scalability and portability.
- **pytest**: Framework for testing API endpoints.

## Prerequisites

- Python 3.9+
- Docker (optional for containerization)
- Git (to clone the repository)

## Installation

### 1. Clone the Repository

Clone the repository from GitHub to your local machine:

```bash
git clone https://github.com/Engmhabib/RAG-agent-using-CrewAi-and-Groq.git
cd RAG-agent-using-CrewAi-and-Groq
