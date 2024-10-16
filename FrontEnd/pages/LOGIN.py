import streamlit as st
import requests

def loadCSS(filepath=""):
    with open(filepath) as file:
        st.markdown(f"<style> {file.read()} </style>", unsafe_allow_html=True)

# Load the css files
loadCSS("FrontEnd/css/style.css")

def sendCredentials(username, password):
    url = "http://localhost:8000/login"
    data = {
        "username": username,
        "passwd": passwd
    }
    resp = requests.post(url=url, json=data).json()
    if resp['status_code'] == 301:
        st.success("LOGIN SUCCESSFUL")
        return resp
    else:
        error.error("Invalid Credentials")

st.title("Login Page")
username = st.text_input("Username")
password = st.text_input("Password", type="password")
error = st.empty()

if st.button("Login"):
    sendCredentials(username, password)
