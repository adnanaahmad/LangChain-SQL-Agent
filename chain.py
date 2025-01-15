import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain_community.tools.sql_database.tool import QuerySQLDatabaseTool
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import create_sql_query_chain
from operator import itemgetter


# Load environment variables from the .env file
load_dotenv()

# Access the API key
api_key = os.getenv("GEMINI_API_KEY")

# Setup
db = SQLDatabase.from_uri("sqlite:///project.db")
llm = ChatGoogleGenerativeAI(model="gemini-pro", api_key=api_key)

# Tools
execute_query = QuerySQLDatabaseTool(db=db)
write_query = create_sql_query_chain(llm, db)

# Prompt for generating answers
answer_prompt = PromptTemplate.from_template(
    """Given the following user question, corresponding SQL query, and SQL result, answer the user question.

Question: {question}
SQL Query: {query}
SQL Result: {result}
Answer: """
)

# Chain setup
answer = answer_prompt | llm | StrOutputParser()
chain = (
    RunnablePassthrough.assign(query=write_query)
    .assign(query=lambda inputs: inputs['query'].replace("```sql\n", "").replace("\n```", ""))
    .assign(result=itemgetter("query") | execute_query)
    | answer
)

# Execution
try:
    response = chain.invoke({"question": "Give users who have age under 30, their id, and also which car they own"})
    print("Response:", response)
except Exception as e:
    print("Error during chain execution:", e)