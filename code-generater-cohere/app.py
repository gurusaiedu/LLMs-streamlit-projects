import streamlit as st
import cohere

st.title("Gen-AI application, for code generation  ")
input=st.text_input("can i know what program your looking for ?") 
cohere_api_key="btu0gWrLzedOkMOrjGC1k6gEhVbIcR0GdsrNlT24"

# initialize the Cohere Client with an API Key
co = cohere.Client(cohere_api_key)

prompt='develop a full function java code for '+input

# generate a prediction for a prompt
prediction = co.chat(message=prompt)

# print the predicted text
print(f'Chatbot: {prediction.text}')

st.write(prediction.text)