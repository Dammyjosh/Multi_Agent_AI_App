A multi Agent App that allows you decide your AI Agent and choose the LLM model version of your choice to generate response from queries.

--- 

## Tech stack
langchain-groq
langchain-community
python-dotenv
uvicorn
fastapi
pydantic
streamlit
langgraph
langchain-core

---

## RUN VIA DOCKER
1. Pull image from dockerhub

docker pull damton/multi-agent-app

2. Run app on local machine
For a Streamlit app (default port 8501):

docker run -p 8501:8501 damton/multi-agent-app
Access the app at:
➡️ http://localhost:8501
