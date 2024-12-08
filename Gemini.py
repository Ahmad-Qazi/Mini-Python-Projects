import streamlit as st
import google.generativeai as genai
genai.configure(api_key="AIzaSyDtLYbM55KYT4SUrQ7kRQ5zltgk-Yxa3ak")
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat()
st.header("Gemini LLM Application")
# input = st.text_input("Input: ", key="input")
prompt = st.text_input("",placeholder="Enter a prompt", key="input")
submit = st.button("Ask the question")
if submit and prompt:
    response = chat.send_message(prompt)
    st.subheader("The Response is")
    st.write(response.text)