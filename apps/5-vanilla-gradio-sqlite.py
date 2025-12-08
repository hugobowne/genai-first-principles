import os, sqlite3, uuid, datetime
from dotenv import load_dotenv
import google.generativeai as genai
import gradio as gr
import fitz

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Use absolute path for DB_FILE relative to this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, "data/interactions.db")
os.makedirs(os.path.dirname(DB_FILE), exist_ok=True) # Ensure directory exists

def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS interactions 
                      (id TEXT PRIMARY KEY, timestamp TEXT, pdf_name TEXT, query TEXT, response TEXT)''')
init_db()

def log_interaction(pdf_name, query, response):
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("INSERT INTO interactions VALUES (?, ?, ?, ?, ?)", 
                    (str(uuid.uuid4()), datetime.datetime.now().isoformat(), pdf_name, query, response))

def extract_text(pdf_path):
    return "".join([page.get_text() for page in fitz.open(pdf_path)])

def query_gemini(query, pdf_file):
    if not pdf_file: return "Please upload a PDF."
    text = extract_text(pdf_file)
    prompt = f"Context:\n{text}\n\nAnswer query based on context:\nQuery: {query}\nAnswer:"
    response = genai.GenerativeModel('gemini-2.5-flash').generate_content(prompt).text
    log_interaction(os.path.basename(pdf_file), query, response)
    return response

gr.Interface(
    fn=query_gemini,
    inputs=[gr.Textbox(label="Query"), gr.File(label="Upload PDF", file_types=[".pdf"])],
    outputs=gr.Textbox(label="Answer", lines=15),
    title="Gemini PDF Query + SQLite Log"
).launch()

