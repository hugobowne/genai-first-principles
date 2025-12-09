# Building Generative AI Applications from First Principles

A workshop repository for learning to build AI-powered applications through hands-on experience.

## Description:
This workshop teaches data and software folk how to build and iterate on generative AI applications using first-principles thinking.

## What You'll Learn:
- How to integrate AI models and APIs into practical applications
- Techniques to manage non-determinism and optimize outputs through prompt engineering
- How to monitor, log, and evaluate AI systems to ensure reliability
- The importance of structured outputs and function calling in AI models
- The software engineering side of building AI systems, including iterative development and debugging
- Multi-LLM workflows and agentic patterns

## Workshop Structure

The workshop is divided into 4 hands-on notebooks, guiding you from basic queries to complex agentic workflows:

*   **Notebook 1: Abstractions vs. First Principles**
    *   Build a simple RAG app using LlamaIndex.
    *   Peel back the layers to rebuild it in Vanilla Python.
    *   Add a frontend (Gradio) and observability (SQLite/Datasette).
    *   *Note:* We'll be running standalone Python applications from the `apps/` directory for this section.
    *   *Key Takeaway:* Understanding what actually happens inside an LLM app by removing the abstractions.

*   **Notebook 2: Prompt Engineering & Evaluation**
    *   Build a two-stage pipeline: Extract structured data from LinkedIn profiles -> Generate personalized emails.
    *   Implement an **LLM-as-a-Judge** to automatically evaluate email quality.
    *   *Key Takeaway:* How to control output structure and automate quality testing.

*   **Notebook 3: Function Calling (Tool Use)**
    *   Teach LLMs to use external tools (Weather API, Tavily Search).
    *   Understand the "Define -> Request -> Execute -> Respond" loop.
    *   *Key Takeaway:* Connecting LLMs to the real world and enriching data.

*   **Notebook 4: Building Agents**
    *   Combine everything into an autonomous Agent.
    *   Build a ReAct agent that can reason, plan, and use tools to solve multi-step problems.
    *   *Key Takeaway:* Moving from linear pipelines to dynamic, autonomous systems.
    
**Note:** There are accompanying slides that will be shared during the workshop.

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

---
### 📚 Continue Learning
> Want to go deeper? Check out our **Building AI Applications** course. It’s a live cohort with hands-on exercises and office hours.
>
> [**Get 35% off with this link**](https://maven.com/hugo-stefan/building-ai-apps-ds-and-swe-from-first-principles?promoCode=genaigh) for workshop participants.

