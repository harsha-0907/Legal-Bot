import streamlit as st

def loadCSS(filepath=""):
    with open(filepath) as file:
        st.markdown(f"<style> {file.read()} </style>", unsafe_allow_html=True)

loadCSS("css/style.css")

# Set the title for this page
st.title("Chat with Us!")

# Input for chat
user_input = st.text_input("Ask me anything:")


if user_input:
    st.write(f"You asked: {user_input}")
    st.write("I'm here to help! :)")