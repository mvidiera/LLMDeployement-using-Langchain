#using streamlit to develop chatbot and include all concepts and create chatbot

# Q&A chatbot

from langchain.llm import OpenAI

from dotenv import load_dotenv

load dotenv()  #take enviroment variables from .env. As soon as I call this, it takes env variable

import streamlit as st

# creating a fucntion to load OpenAI model and get responses

def get_openai_response(question):
    llm= OpenAI(openai_api_key= os.getenv("OPEN_API_KEY"), model_name = "text-davinci-003",temperature= 0.5)

    #next is to get response
    response= llm(question)
    return response

#initialising streamlit app

st.set_page_config(page_title= "Q&A Demo")

st.header("Langchain Application")

# Capture input text and then user will click on answer the question button

input= st.text_input("Input: ", key="input")
#take this input and call, response() defined above along with IP as parameter
response= get_openai_response(input)

#create submit button
submit= st.button("Ask the question")

# If ask button is clicked, if true, then 

if submit: 
    st.subheader("The response is ")
    st.write(response)
                                           