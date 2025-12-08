"""
Query documents using LlamaIndex with Anthropic Claude LLM.
"""
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.anthropic import Anthropic

# Load documents and build the vector index
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)

# Initialize the Claude LLM
claude_llm = Anthropic(model="claude-sonnet-4-5")

# Create query engine and execute query
query_engine = index.as_query_engine(llm=claude_llm)
response = query_engine.query("tell me everything about this person")

print(response)