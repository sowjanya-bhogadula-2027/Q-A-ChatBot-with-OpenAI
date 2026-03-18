import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv
load_dotenv()

#langsmith tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="Q&A Chatbot With OPENAI"

#propmt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the user queries."),
        ("user","Question:{question}")
    ]
)

def generate_response(question,api_key,engine,temperature,max_tokens):
    openai.api_key=api_key
    llm=ChatOpenAI(model=engine)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer

#streamlit APP
#title
st.title("Q&A ChatBot with OpenAI")

#sidebar settings
st.sidebar.title("Settings")
api_key=st.sidebar.text_input("Enter your Open AI API Key:",type="password")

#model
engine=st.sidebar.selectbox("Select an OpenAI model",["gpt-5.4","gpt-5.4-mini","gpt-5.4-nano"])

#slider for temparature
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens=st.sidebar.slider("Maximum Tokens",min_value=50,max_value=300,value=150)

#main interface for user interaction
st.write("Ask any question")
user_input=st.text_input("You: ")

if user_input:
    response=generate_response(user_input,api_key,engine,temperature,max_tokens)
    st.write(response)
else:
    st.write("Please provide the user input")
