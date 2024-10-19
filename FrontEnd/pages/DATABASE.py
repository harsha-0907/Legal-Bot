# These are the various judgments form the SC and the High Court
import pandas as pd
import streamlit as st

def loadCSS(filepath=""):
    with open(filepath) as file:
        st.markdown(f"<style> {file.read()} </style>", unsafe_allow_html=True)


loadCSS("FrontEnd/css/style.css")

data = pd.read_csv("FrontEnd/pages/db_data.csv")


st.title("Judgments from SC and High Court")
st.subheader("Here are the URLs from the CSV")

st.dataframe(data)

st.markdown("<h3 text-allign=right> Total: 47000 references </h3>", unsafe_allow_html=True)