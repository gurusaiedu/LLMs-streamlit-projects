import streamlit as st

from langchain.chains import LLMChain
from langchain.chat_models import ChatCohere
from langchain.prompts import PromptTemplate

st.title(" Genarate program in any language")
question=st.text_input("can i know what program your looking for ?") 
language=st.text_input("language") 
cohere_api_key="btu0gWrLzedOkMOrjGC1k6gEhVbIcR0GdsrNlT24"

# initialize the Cohere Client with an API Key
llm=ChatCohere(cohere_api_key=cohere_api_key,
               temperature=0)

prompt_templet_string1="let's consider your good programmder, \
develop a working {language} program for {question} \
"
from langchain.prompts import ChatPromptTemplate
prompt_templet= ChatPromptTemplate.from_template(prompt_templet_string1)
customer_messages=prompt_templet.format_messages(language=language,question=question)
reponse=llm(customer_messages)



st.write(reponse.content)