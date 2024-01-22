import streamlit as st
from dotenv import load_dotenv
load_dotenv()


import os
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Funtion to load Gemini model and Gemini pro molde and get response 
model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text


st.set_page_config(page_icon="😊",
                   page_title="Gemini pro Q&A demo")

st.header("Gemini LLM Application")

input = st.text_input("Input:-", key="input")
submit = st.button("Ask the Question")


if submit:
    resp_op = get_gemini_response(input)
    st.subheader("The Response is :-")
    st.write(resp_op)
