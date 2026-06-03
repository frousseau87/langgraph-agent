import os

from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent

llm = ChatOllama(
    model=os.getenv("OLLAMA_MODEL", "llama3"),
    base_url=os.getenv("OLLAMA_BASE_URL", "http://172.24.208.1:11434"),
)

# Agent ReAct sans tools pour commencer
agent = create_react_agent(llm, tools=[])

# Test
response = agent.invoke({
    "messages": [{"role": "user", "content": "Explique-moi ce qu'est LangGraph en 3 phrases."}]
})

print(response["messages"][-1].content)