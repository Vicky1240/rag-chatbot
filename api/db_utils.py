import sqlite3
from datetime import datetime
from sqlalchemy import create_engine,text
import os


# Fetch MySQL connection details from environment variables
username = os.getenv("MYSQL_USERNAME")
password = os.getenv("MYSQL_PASSWORD")
host = os.getenv("MYSQL_HOST")
database = os.getenv("MYSQL_DATABASE")

# Create a connection string
connection_string = f'mysql+mysqlconnector://{username}:{password}@{host}/{database}'

# Create an engine
engine = create_engine(connection_string)


# Create the application_logs table
def create_application_logs():
    with engine.connect() as conn:
        conn.execute(text('''
            CREATE TABLE IF NOT EXISTS application_logs (
                id INT AUTO_INCREMENT PRIMARY KEY,
                session_id VARCHAR(255) NOT NULL,
                user_query TEXT NOT NULL,
                gpt_response TEXT NOT NULL,
                model VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        '''))
        conn.close()

# Insert a log into the application_logs table
def insert_application_logs(session_id, user_query, gpt_response, model):
    with engine.connect() as conn:
        conn.execute(text('''
            INSERT INTO application_logs (session_id, user_query, gpt_response, model)
            VALUES (:session_id, :user_query, :gpt_response, :model)
        '''), {
            "session_id": session_id,
            "user_query": user_query,
            "gpt_response": gpt_response,
            "model": model
        })
        conn.commit()
        conn.close()

# Retrieve chat history for a specific session_id
def get_chat_history(session_id):
    with engine.connect() as conn:
        result = conn.execute(text('''
            SELECT user_query, gpt_response
            FROM application_logs
            WHERE session_id = :session_id
            ORDER BY created_at
        '''), {"session_id": session_id}).mappings()
        messages = []
        for row in result:
            messages.extend([
                {"role": "human", "content": row['user_query']},
                {"role": "ai", "content": row['gpt_response']}
            ])
        conn.close()
        

    return messages

def create_document_store():
    with engine.connect() as conn:
        conn.execute(text('''CREATE TABLE IF NOT EXISTS document_store
                    (id INTEGER PRIMARY KEY AUTO_INCREMENT,
                     filename TEXT,
                     upload_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)'''))
        conn.close()

def insert_document_record(filename):
    with engine.connect() as conn:
        result = conn.execute(
            text('INSERT INTO document_store (filename) VALUES (:filename)'),
            {"filename": filename}
        )
        conn.commit()
        conn.close()
        return result.lastrowid

def delete_document_record(file_id):
    with engine.connect() as conn:
        conn.execute(text('DELETE FROM document_store WHERE id = :file_id'), {"file_id": file_id})
        conn.commit()
        conn.close()
        return True

def get_all_documents():
    with engine.connect() as conn:
        result = conn.execute(
            text('''
                SELECT id, filename, upload_timestamp 
                FROM document_store 
                ORDER BY upload_timestamp DESC
            ''')
        )
        documents = [
            {"id": row["id"], "filename": row["filename"], "upload_timestamp": row["upload_timestamp"]}
            for row in result.mappings()
        ]
    return documents

# Initialize the database tables
create_application_logs()
create_document_store()
