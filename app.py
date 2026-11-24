from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
import streamlit as st
from dotenv import load_dotenv
 
load_dotenv()
 
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
 
llm1=ChatOpenAI(model="gpt-4o-mini")
 
prompt=ChatPromptTemplate.from_messages([
 
    ("system","You are health expert, answer user queries only if the queries are related to health"),
    ("user","{input}")
])
 
parser=StrOutputParser()
 
chain= prompt |llm1 |parser
 
st.title("Health Expert")
input=st.text_input("Ask your query")
 
if input:
    st.write(chain.invoke({"input":input}))
# python -m streamlit run app.py --server.address 0.0.0.0 --server.port 8000 --server.headless true
