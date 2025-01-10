
# **RAG Chatbot with FastAPI, LangChain, and Streamlit**

## **Overview**

This project implements a Retrieval-Augmented Generation (RAG) chatbot using FastAPI, LangChain, and Streamlit. The chatbot enhances language model responses by integrating external document retrieval, providing accurate and context-rich answers. A Streamlit-based interface allows for an interactive and user-friendly way to query and interact with the chatbot.

---

## **Features**

- **Document Management**: Upload, index, and manage documents to build a knowledge base.
- **Chat Interface**: Interact with the chatbot through a Streamlit-based UI or API endpoints.
- **Asynchronous Processing**: Efficient handling of multiple requests using FastAPI's asynchronous capabilities.
- **Extensibility**: Modular design allows for easy integration of additional features and components.

---

## **File Structure**

```
project-directory/
├── api/
│   ├── chroma_utils.py
│   ├── db_utils.py
│   ├── langchain_utils.py
│   ├── main.py
│   ├── pydantic_models.py                
├── app/
│   ├── api_utils.py  
│   └── chat_interface.py
│   ├── sidebar.py
│   ├── streamlit_app.py
└── .env    
└── requirements.txt
```

### **API Folder (`api/`)**
- **`chroma_utils.py`**: Utilities for managing ChromaDB operations, including vector storage and retrieval.
- **`db_utils.py`**: Functions for database interactions, managing chat history and document metadata.
- **`langchain_utils.py`**: Implements the RAG chain using LangChain components.
- **`main.py`**: Entry point for the FastAPI application, defining API routes and initializing components.
- **`pydantic_models.py`**: Defines data models with Pydantic for request validation and type enforcement.

### **Streamlit Application Folder (`app/`)**
- **`streamlit_app.py`**: Main Streamlit application for interacting with the chatbot.
- **`chat_interface.py`**: Logic for handling the conversation between the user and the chatbot.
- **`sidebar.py`**: Manages user input and settings in the Streamlit app's sidebar.
- **`api_utils.py`**: Utility functions for interacting with the FastAPI backend.

---

## **Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/rag-chatbot.git
   cd rag-chatbot
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   - Create a `.env` file in the root directory.
   - Add necessary environment variables, such as API keys and database connection strings.

4. **Initialize the Database**:
   - Ensure that the `chroma_db/` directory exists for ChromaDB persistence.
   - If using an SQL database for chat history, set up the database and run migrations as needed.

---

## **Usage**

1. **Start the FastAPI Application**:
   ```bash
   uvicorn api/main:app --reload
   ```

2. **Run the Streamlit Application**:
   ```bash
   streamlit run app/streamlit_app.py
   ```

3. **Access the API Documentation**:
   - Navigate to `http://localhost:8000/docs` to explore the available endpoints and interact with the API.

4. **Interact with the Chatbot**:
   - Use the Streamlit interface at `http://localhost:8501` to interact with the chatbot.
   - Upload documents via the interface or API for enhanced chatbot responses.
---

## **Technologies Used**

- **FastAPI**: Web framework for building the API.
- **LangChain**: Framework for building applications powered by language models.
- **Streamlit**: Framework for building a user-friendly web interface.
- **ChromaDB**: Vector database for storing and retrieving document embeddings.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **Python Libraries**: Including `docx2txt`, `pypdf`, `python-multipart`, `streamlit`, and more.

---
