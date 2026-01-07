import streamlit as st  
import dotenv #We use dotenv to securely manage sensitive configuration values like API keys by loading them from environment variables instead of hardcoding them in source code.

import langchain

from dotenv import load_dotenv #it will load all the environment variables from .env file
load_dotenv() #(Search .env file)

import os
os.environ["GOOGLE_API_KEY"] =os.getenv("gemini")

from langchain_google_genai import GoogleGenerativeAI , ChatGoogleGenerativeAI 

st.set_page_config(page_title="Chat Bot",page_icon="🤖")
# Set page title: it will be displayed on the browser tab


st.title("🤖 Chat Bot with langchain and streamlit")

#The below code initializes a session-level variable in Streamlit to store conversation history. It ensures the list is created only once and persists across reruns of the app.
# store memory:
if "conv" not in st.session_state: #session_state :It is a dictionary-like object provided by Streamlit
    st.session_state["conv"]=[] #Creates an empty list to store chat messages, example:["Hi", "Hello", "How are you?"]
    st.session_state["memory"]=[] #Creates another list for LLM memory
    st.session_state["memory"].append(("system","Act as a senior-level, 5+ years experienced Data Science Engineer")) #Sets the system prompt : Controls model behavior

#session_state{"conv" : [{"role":"user" ,"content":prompt},{"role":"ai" ,"content":response.content}] , memory =[("system","Act like a 5 year old child"),("user",prompt),("ai",response.content)]"}

for y in st.session_state["conv"]: #For chat effect
    
    with st.chat_message(y["role"]):
        st.write(y["content"])



prompt = st.chat_input("Type your queries")

if prompt:
    st.session_state["conv"].append({"role":"user" ,"content":prompt})
    st.session_state["memory"].append(("user",prompt))
    
    with st.chat_message("user"):
        st.write(prompt)
    
    model = ChatGoogleGenerativeAI(model ="gemini-2.5-flash-lite")
    
    response = model.invoke(st.session_state["memory"])
    
    with st.chat_message("ai"):
        st.write(response.content)
    
    st.session_state["conv"].append({"role":"ai" ,"content":response.content})
    st.session_state["memory"].append(("ai",response.content))
    