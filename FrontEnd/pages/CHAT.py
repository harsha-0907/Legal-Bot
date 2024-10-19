import streamlit as st
import json
import requests
import streamlit.components.v1 as components

# Load custom CSS (if any)
def loadCSS(filepath=""):
    with open(filepath) as file:
        st.markdown(f"<style> {file.read()} </style>", unsafe_allow_html=True)

loadCSS("FrontEnd/css/style.css")  # Assuming you have a CSS file to load

token = st.session_state.jwt_token if 'jwt_token' in st.session_state else None

if token:
    st.write("Welcome")
else:
    st.write("(Please Login First)")

def send_request(data, token=None):

    url = "http://localhost:8000/chat"
    headers = {
        "Authorization": f"Bearer {token}" if token else ""
    }
    
    response = requests.post(url, json=data, headers=headers)
    content = json.loads(response.content.decode('utf-8'))
    #print(response, type(content))
    return content
    

# Function to display messages in the required format (request, response in order)
def display_messages(chats):
    for i, chat in enumerate(chats):
        # Display request (question) in the top-right
        st.markdown(f"<div style='text-align: right;'>**Request {i+1}:** {chat['question']}</div>", unsafe_allow_html=True)
        
        # Display response (response) in the bottom-left, aligned with the request
        st.markdown(f"<div style='text-align: left;'>**Response {i+1}:** {chat['response']}</div>", unsafe_allow_html=True)

# UI elements
st.title("Let's Have a Conversation .!")

# Input from the user for a message request
user_input = st.text_input("Enter your message:")

if st.button("Send") and user_input:
    if token:
        request_data = {
            "message": user_input
        }
        response = send_request(request_data, token)
        print(response, response['status_code'])
        chats = []
        if response['status_code'] == 200:
            chats = response['chats']

        display_messages(chats)
    else:
        print("Please Login")
