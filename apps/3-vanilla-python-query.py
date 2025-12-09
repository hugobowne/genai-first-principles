import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load the file content
with open("data/hba.txt", "r") as f:
    document_text = f.read()

# Create the prompt with context
prompt = f"""
Context information is below.
---------------------
{document_text}
---------------------
Given the context information and not prior knowledge, answer the query.
Query: tell me everything about this person.
Answer:
"""

# Call the API
model = genai.GenerativeModel('gemini-2.5-flash')
response = model.generate_content(prompt)

print(response.text)

