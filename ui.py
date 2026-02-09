from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt, PromptTemplate
load_dotenv()

model = ChatOpenAI(model = 'gpt-5-mini', temperature= 0.3)

st.header("SMART  SHOPPING AI ASSISTANT")
user_input = st.text_area("Enter your input here: ")
if st.button("Send ->"):
    result = model.invoke(user_input)
    st.write(result.content)