# Building Generative AI Applications from First Principles

A workshop repository for learning to build LLM-powered applications through hands-on experience.

## Description:
This workshop teaches data and software folk how to build and iterate on generative AI applications using first-principles thinking. You'll learn prompt engineering, evaluation, monitoring, and handling non-determinism through building a complete PDF-querying application. All techniques are generalizable to other AI applications.

## What You'll Learn:
- How to integrate AI models and APIs into practical applications
- Techniques to manage non-determinism and optimize outputs through prompt engineering
- How to monitor, log, and evaluate AI systems to ensure reliability
- The importance of structured outputs and function calling in AI models
- The software engineering side of building AI systems, including iterative development and debugging
- Multi-LLM workflows and agentic patterns

## Prerequisites:
- Basic Python programming knowledge
- Familiarity with REST APIs
- Experience with Jupyter Notebooks (preferred but not required)
- No prior AI/ML experience required

## Setup Instructions

### Option 1: GitHub Codespaces (Recommended)
1. **Create a Codespace**
   - Click **Code** → **Create Codespace on main**

2. **Activate the Environment**
   ```bash
   source .venv/bin/activate
   ```

3. **Set Up API Keys**
   ```bash
   export OPENAI_API_KEY="your-key-here"
   export ANTHROPIC_API_KEY="your-key-here"
   export GOOGLE_API_KEY="your-key-here"
   export TAVILY_API_KEY="your-key-here"
   ```

### Option 2: Local Setup
1. **Create Virtual Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install Dependencies**
   ```bash
   # Recommended: Install with UV (faster)
   pip install uv
   uv pip install -r requirements.txt

   # Or use regular pip
   pip install -r requirements.txt
   ```

3. **Set Up API Keys**
   
   Create a `.env` file from the example:
   ```bash
   cp .env.example .env
   ```
   
   Then open `.env` and add your API keys:
   ```bash
   OPENAI_API_KEY="your-key-here"
   ANTHROPIC_API_KEY="your-key-here"
   GOOGLE_API_KEY="your-key-here"
   TAVILY_API_KEY="your-key-here"
   ```
