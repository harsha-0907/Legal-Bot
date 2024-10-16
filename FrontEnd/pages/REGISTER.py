# For the Register page

import streamlit as st

def loadCSS(filepath=""):
    with open(filepath) as file:
        st.markdown(f"<style> {file.read()} </style>", unsafe_allow_html=True)

# Load the css files
loadCSS("FrontEnd/css/style.css")

def registerUser(username, passwd):
    # Register the User


st.title("Welcome.. Let's get you Registered")
username = st.text_input("Username")
note = st.empty()

if st.button("Proceed"):
    # Check if the username is already taken
    resp = requests.post(url="http://localhost:89/register/check-user", json={'username': username})
    if resp.status_code == 404:
        note.write("Username is already Taken")
        # Add way to refresh the whole page
    elif resp.status_code == 200:
        note.write(f"Thats a good choice {username}. {resp.message}")
        password = st.text_input("Password")
        if st.button("Register"):
            # If the user is ready to register
            resp = requests.post(url="http://localhost:89/register", json={'username': username, 'passwd': passwd})
            if 
            st.success("Regitration Successfull")
            jwt_token = generateJWTToken(username)
            response = RedirectResponse("/CHAT")
            response.headers["Authorization"] = f"Bearer {jwt_token}"
            return response
                   
