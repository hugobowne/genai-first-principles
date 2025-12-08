import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai
import google.generativeai as genai_old # keeping for compatibility if needed, but using new client

load_dotenv()

def extract_text_gemini(pdf_path: Path) -> str:
    api_key = os.getenv("GOOGLE_API_KEY")
    client = genai.Client(api_key=api_key)
    
    uploaded = client.files.upload(file=pdf_path)
    
    # Using Gemini 2.5 Flash as verified earlier
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            uploaded,
            (
                "Extract all text in reading order. Return Markdown (preserve headings, lists, tables). "
                "Do not summarize. For each image encountered, insert a placeholder like [IMAGE 1], [IMAGE 2] "
                "in the order they appear, and include a brief description of the image plus any visible "
                "caption/title/figure number next to the placeholder."
            ),
        ],
    )
    
    # Cleanup
    client.files.delete(name=uploaded.name)
    return response.text

if __name__ == "__main__":
    pdf_path = Path("data/BIT-AI-2025-summary.pdf")
    
    if pdf_path.exists():
        text = extract_text_gemini(pdf_path)
        print(text)
        
        # Optionally save to file
        with open("extracted_text.txt", "w") as f:
            f.write(text)
    else:
        print(f"PDF not found at {pdf_path}")
