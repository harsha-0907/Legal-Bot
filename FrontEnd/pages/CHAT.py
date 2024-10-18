import streamlit as st
import json
import requests

def loadCSS(filepath=""):
    with open(filepath) as file:
        st.markdown(f"<style> {file.read()} </style>", unsafe_allow_html=True)

loadCSS("FrontEnd/css/style.css")

js_script = """
<script>
  const token = window.localStorage.getItem('my_token');
  window.parent.postMessage({ token: token }, '*');
</script>
"""

# Inject JS to get token from localStorage
st.components.v1.html(js_script, height=0)

# Fetch JWT token from localStorage using the postMessage mechanism
token = None
if 'jwt_token' in st.session_state:
    token = st.session_state.jwt_token

# Function to send request with JWT token
def send_request(data, token=None):
    url = "https://your-backend-endpoint.com/api"
    
    headers = {
        "Authorization": f"Bearer {token}" if token else ""
    }
    
    response = requests.post(url, json=data, headers=headers)
    return response.json()

# Function to display messages in the required format (req, resp in the desired order)
def display_messages(chats):
    # Split the chats into requests and responses
    for i, chat in enumerate(chats):
        # Display request (question) in the top-right
        st.markdown(f"<div style='text-align: right;'>**Request {i+1}:** {chat['question']}</div>", unsafe_allow_html=True)
        
        # Display response (response) in the bottom-left, aligned with the request
        st.markdown(f"<div style='text-align: left;'>**Response {i+1}:** {chat['response']}</div>", unsafe_allow_html=True)

# UI elements
st.title("JWT Auth and Message Formatter")

# Input from the user for a message request
user_input = st.text_input("Enter your message:")

if st.button("Send Request") and user_input:
    # Constructing a message request
    request_data = {
        "message": user_input
    }
    
    # Send the request to the backend
    response = send_request(request_data, token)
    
    # Assuming the response is in the form of ChatModel with a list of Chat objects
    chats = response.get('chats', [])  # Extract chats from the response
    
    # Display the messages in the desired format
    display_messages(chats)