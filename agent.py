import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.utilities import SQLDatabase

# Load environment variables from the .env file
load_dotenv()

# Access the API key
api_key = os.getenv("GEMINI_API_KEY")

# Setup
db = SQLDatabase.from_uri("sqlite:///project.db")
llm = ChatGoogleGenerativeAI(model="gemini-pro", api_key=api_key)


agent_executor = create_sql_agent(llm, db=db, verbose=True)

agent_executor.invoke(
    {
        "input": "Give users who have age under 30, their id, and also which car they own"
    }
)