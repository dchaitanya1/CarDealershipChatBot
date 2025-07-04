from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
from langchain.prompts.prompt import PromptTemplate
from langchain.prompts import FewShotPromptTemplate
import os
from few_shots import few_shots
from dotenv import load_dotenv

load_dotenv(override=True)

print("GOOGLE_API_KEY is:", os.getenv("GOOGLE_API_KEY"))

def get_db_chain():

    llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.0-flash",  # This is the Gemini Flash model
    google_api_key=os.environ["GOOGLE_API_KEY"],
    temperature=0.1
    )

    db_user = "root"
    db_password = "your_db_password"
    db_host = "localhost"
    db_name = "car_dealership"

    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}", sample_rows_in_table_info=3)

    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    to_vectorize = [" ".join(example.values()) for example in few_shots]
    vectorstore = Chroma.from_texts(to_vectorize, embedding=embeddings, metadatas=few_shots)
    example_selector = SemanticSimilarityExampleSelector(
    vectorstore = vectorstore,
    k=2,
    )

    _mysql_prompt = """You are a MySQL expert. Given an input question, first create a syntactically correct MySQL query to run, then look at the results of the query and return the answer to the input question.

Do NOT use markdown formatting (like triple backticks ```sql) in your response. Just give the raw SQL.

Unless the user specifies a specific number of results in the question, query for at most {top_k} results using the LIMIT clause as per MySQL. You may use ORDER BY to return the most informative results.

Never use SELECT * — query only the necessary columns needed to answer the question. Wrap all column names and table names in backticks (`) to denote them as delimited identifiers.

Use only the columns listed in the database schema. Do not invent or assume column names. Be careful about which table each column belongs to.

If the question refers to "today", use the MySQL function CURDATE() for filtering date columns.

Use the following format exactly:

Question: Question here  
SQLQuery: SQL query to run  
SQLResult: Result of the SQLQuery  
Answer: Final answer here

No preamble.
"""



    example_prompt = PromptTemplate(
    input_variables=["Question","SQLQuery","SQLResult","Answer",],
    template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
    )

    few_shot_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix=_mysql_prompt,
    suffix=PROMPT_SUFFIX,
    input_variables=["input", "table_info", "top_k"], #These variables are used in the prefix and suffix
    )
    
    chain = SQLDatabaseChain.from_llm(llm,db,verbose=True,prompt=few_shot_prompt)
    return chain

if __name__ == '__main__':

    chain = get_db_chain()