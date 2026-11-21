# Multi-Agent Research System

A multi-agent research pipeline built with LangChain and LangGraph, with a simple Streamlit UI. Enter a topic and four steps run in order:

1. **Search agent** finds recent, reliable information on the topic.
2. **Reader agent** picks the most relevant URL and scrapes it for deeper content.
3. **Writer chain** drafts a structured report (Introduction, Key Findings, Conclusion, Sources).
4. **Critic chain** reviews the report with a score, strengths, and areas to improve.

## Project structure

```
.
├── app.py          # Streamlit UI
├── pipeline.py     # Runs the 4-step research pipeline
├── agents.py       # Agents, writer chain, critic chain, LLM setup
├── tools.py        # Web search and scraping tools
├── .env            # API keys (not committed)
├── .env.example    # Template for required keys
└── requirements.txt
```

## Setup

1. Clone the repo and create a virtual environment:

   ```
   git clone https://github.com/Joyash22/Multi-Research-Agent.git
   cd Multi-Research-Agent
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project folder (see `.env.example`):

   ```
   GROQ_API_KEY=your_groq_key
   TAVILY_API_KEY=your_search_key
   ```

   Use the key names your `agents.py` and `tools.py` actually read. Never commit `.env`.

## Run

Streamlit UI:

```
streamlit run app.py
```

Terminal only:

```
python pipeline.py
```

## Configuration

The model is set in `agents.py`:

```python
llm = ChatOpenAI(
    model="openai/gpt-oss-120b",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0,
)
```

Use any chat model that supports tool calling. Model names change over time, so check your provider's current model list. To use OpenAI instead, remove `base_url`, set `OPENAI_API_KEY`, and use a model such as `gpt-4o-mini`.

## Security

- Keep API keys only in `.env`, and make sure `.env` is listed in `.gitignore`.
- If a key is ever pushed to a public repo, revoke it and create a new one.

## Tech stack

Python, LangChain, LangGraph, Streamlit, Groq (OpenAI-compatible API), python-dotenv.