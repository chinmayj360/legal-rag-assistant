from langgraph.graph import StateGraph
from retriever import get_retriever
from generator import generate_answer
from router import route_query
from hitl import escalate_to_human

class State(dict):
    pass

retriever = get_retriever()

def process_node(state):
    query = state["query"]
    docs = retriever.invoke(query)
    answer = generate_answer(query, docs)

    state["answer"] = answer
    return state

def route_node(state):
    decision = route_query(state["query"])
    state["route"] = decision
    return state

def hitl_node(state):
    state["answer"] = escalate_to_human(state["query"])
    return state

builder = StateGraph(State)

builder.add_node("route", route_node)
builder.add_node("process", process_node)
builder.add_node("hitl", hitl_node)

builder.set_entry_point("route")

builder.add_conditional_edges(
    "route",
    lambda state: state["route"],
    {
        "answer": "process",
        "escalate": "hitl"
    }
)

builder.set_finish_point("process")
builder.set_finish_point("hitl")

graph = builder.compile()