"""
Query documents using Google Gemini for embeddings and LLM.
"""
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding

# Set up the embedding model
embed_model = GoogleGenAIEmbedding(
    model_name="text-embedding-004",
    embed_batch_size=8)

# Load documents and build the vector index
documents = SimpleDirectoryReader("data/").load_data()
index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)

# Initialize the Gemini LLM
gemini_llm = GoogleGenAI(model="gemini-2.5-flash")

# Create query engine and execute query
query_engine = index.as_query_engine(llm=gemini_llm)
response = query_engine.query("tell me everything about this person")

print(response)