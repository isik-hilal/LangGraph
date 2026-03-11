import os
from typing import TypedDict, List, Dict, Any, Optional, Union
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()


class AgentState(TypedDict): 
    messages: List[Union[HumanMessage, AIMessage]]

llm =ChatOpenAI(model="gpt-4o")

def process(state: AgentState) -> AgentState:
    """ Thid node will solve the request you input"""
    response =llm.invoke(state["messages"])
    state["messages"].append(AIMessage(content=response.content))
    print(f"\nAI:{response.content}")
    return state

graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process") 
graph.add_edge("process", END)

agent = graph.compile()

# starting from here it gets different from the previous one

conversation_history=[]

user_input= input("Enter: ")
while user_input!= "exit":
    conversation_history.append(HumanMessage(content=user_input))
    result= agent.invoke({'messages':conversation_history})
    conversation_history= result["messages"]
    user_input= input("Enter: ")
    