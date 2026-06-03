# langgraph-agent

Agent ReAct minimal avec [LangGraph](https://github.com/langchain-ai/langgraph) et Ollama (modèle local).

## Prérequis

- Python 3.12+
- [Ollama](https://ollama.com/) avec le modèle `llama3` (ou autre, à configurer)

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Adaptez `OLLAMA_BASE_URL` dans `.env` si Ollama tourne sur un autre hôte (souvent l’IP Windows depuis WSL).

## Lancement

```bash
python agent.py
```
