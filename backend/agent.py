from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from tools import drive_search_tool
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0
)

tools = [drive_search_tool]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)