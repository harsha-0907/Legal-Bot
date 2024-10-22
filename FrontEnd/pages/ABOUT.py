import streamlit as st
#import pandas as pd

def loadCSS(filepath=""):
    with open(filepath) as file:
        st.markdown(f"<style> {file.read()} </style>", unsafe_allow_html=True)

loadCSS("FrontEnd/css/style.css")
st.title("All About Us !")

st.header("Who Are We")
st.write("We are the students of MVGR!!! We a team of explorers who love solving problems that bring about a change. We are Passionate and Eveready to take on new challenges!!!")

st.markdown("<br></br>", unsafe_allow_html=True)
st.header("Why Legal-Bot??")
st.write("Access to legal guidance is often limited by cost, complexity, and availability. A legal bot can democratize this access, providing affordable, immediate, and reliable legal assistance to everyone, regardless of their financial background. By automating routine legal tasks, it lowers the barrier to access quality legal support, ensuring that individuals and small businesses alike can make informed decisions without the burden of expensive legal fees")

st.markdown("<br></br>", unsafe_allow_html=True)
st.header("Thanks for Knowing About Us!!!")