import os
from dotenv import load_dotenv
import google.generativeai as genai
import gradio as gr
import fitz  # PyMuPDF

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def query_gemini(query, pdf_file):
    if pdf_file is None:
        return "Please upload a PDF file."
        
    # Extract text from the uploaded PDF
    document_text = extract_text_from_pdf(pdf_file)

    # Create the prompt with context
    prompt = f"""
    Context information is below.
    ---------------------
    {document_text}
    ---------------------
    Given the context information and not prior knowledge, answer the query.
    Query: {query}
    Answer:
    """

    # Call the API
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content(prompt)
    return response.text

# Create Gradio Interface
iface = gr.Interface(
    fn=query_gemini,
    inputs=[
        gr.Textbox(label="Query", placeholder="Ask a question about the PDF..."),
        gr.File(label="Upload PDF", file_types=[".pdf"])
    ],
    outputs=gr.Textbox(label="Answer", lines=15),
    title="Gemini 2.5 Flash PDF Query",
    description="Upload a PDF and ask questions about it."
)

if __name__ == "__main__":
    iface.launch()

