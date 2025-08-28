from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults

from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

from langchain_core.messages import HumanMessage, SystemMessage

from app.config.settings import settings

def get_response_from_ai_agents(llm_id, query, allow_search, system_prompt):
    llm = ChatGroq(model=llm_id)

    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    agent = create_react_agent(
        model=llm,
        tools=tools
    )

    # system prompt as SystemMessage + user messages as HumanMessages
    state = {
        "messages": [SystemMessage(content=system_prompt)]
                    + [HumanMessage(content=msg) for msg in query]
    }

    response = agent.invoke(state)

    messages = response.get("messages", [])
    ai_messages = [m.content for m in messages if isinstance(m, AIMessage)]

    return ai_messages[-1] if ai_messages else "No AI response generated"