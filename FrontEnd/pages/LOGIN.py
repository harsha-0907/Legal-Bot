import streamlit as st
import requests

def loadCSS(filepath=""):
    with open(filepath) as file:
        st.markdown(f"<style> {file.read()} </style>", unsafe_allow_html=True)

# Load the css files
loadCSS("FrontEnd/css/style.css")

def sendCredentials(username, password):
    if username == 'admin' and password == 'admin':
        st.success("LOGIN SUCCESSFUL")
    else:
        error.error("Invalid Credentials")

st.title("Login Page")
username = st.text_input("Username")
password = st.text_input("Password", type="password")
error = st.empty()

if st.button("Login"):
    sendCredentials(username, password)

