import streamlit as st
from streamlit.components.v1 import iframe

st.title("My App with Botpress Chatbot")
st.write("Welcome to my app! You can use the chatbot below.")

# Embed the Botpress chatbot
botpress_url = "https://cdn.botpress.cloud/webchat/v2/shareable.html?botId=6c568437-0195-4867-a69e-72c8321ea9a0"
iframe_height = 600

iframe(botpress_url, height=iframe_height)