from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from typing import TypedDict, Annotated
import operator

llm = ChatOllama(
    model="qwen2.5:7b",
    base_url="http://localhost:11434"
)

@tool
def get_weather(city: str) -> str:
    """Retourne la météo d'une ville."""
    return f"Il fait 22°C et ensoleillé à {city}."

tools = [get_weather]
llm_with_tools = llm.bind_tools(tools)

class AgentState(TypedDict):
    messages: Annotated[list, operator.add]

def call_llm(state: AgentState):
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}

def should_continue(state: AgentState):
    last = state["messages"][-1]
    if hasattr(last, "tool_calls") and last.tool_calls:
        return "tools"
    return END

graph = StateGraph(AgentState)
graph.add_node("llm", call_llm)
graph.add_node("tools", ToolNode(tools))
graph.set_entry_point("llm")
graph.add_conditional_edges("llm", should_continue)
graph.add_edge("tools", "llm")

agent = graph.compile()

response = agent.invoke(
    {"messages": [{"role": "user", "content": "Quel temps fait-il à Paris ?"}]},
    {"recursion_limit": 5}
)

for step in agent.stream(
    {"messages": [{"role": "user", "content": "Quel temps fait-il à Paris ?"}]},
    {"recursion_limit": 5}
):
    print(step)

print(response["messages"][-1].content)