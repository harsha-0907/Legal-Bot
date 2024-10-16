import streamlit as st

def loadCSS(filepath=""):
    with open(filepath) as file:
        st.markdown(f"<style> {file.read()} </style>", unsafe_allow_html=True)

loadCSS("FrontEnd/css/style.css")
st.title("WELCOME TO LEGAL BOT")

st.write(" Naviagte to any pages using the NAVBAR")
