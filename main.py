import streamlit as st  
import dotenv #Use for API key management

import langchain

from dotenv import load_dotenv #it will load all the environment variables from .env file
load_dotenv() #call the function once at the start of your code

import os
os.environ["GOOGLE_API_KEY"] =os.getenv("gemini")

from langchain_google_genai import GoogleGenerativeAI , ChatGoogleGenerativeAI 



st.title("Simple Gemini Model as a regular model ")

prompt = st.text_area("Type any query here")

if st.button("Generate Response"):
    rmodel = GoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=1)
    response = rmodel.invoke(prompt)
    st.write(response)


