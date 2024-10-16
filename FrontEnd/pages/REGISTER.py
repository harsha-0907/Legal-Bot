import streamlit as st
import requests

def loadCSS(filepath=""):
    with open(filepath) as file:
        st.markdown(f"<style> {file.read()} </style>", unsafe_allow_html=True)

# Load the css files
loadCSS("FrontEnd/css/style.css")

st.title("Welcome.. Let's get you Registered")

# Use session state to persist variables across reruns
if 'gotUsername' not in st.session_state:
    st.session_state.gotUsername = False
if 'username' not in st.session_state:
    st.session_state.username = None

note = st.empty()

if not st.session_state.gotUsername:
    # If the username is not set
    st.session_state.username = st.text_input("Username", value=st.session_state.username)
    
    if st.button("Proceed"):
        # Check if the username is already taken
        resp = requests.post(url="http://localhost:8000/register/check-user", json={'username': st.session_state.username})
        resp = resp.json()
        if resp['status_code'] == 404:
            note.write("Username is already Taken")
            # Add way to refresh the whole page (st.experimental_rerun)
        elif resp['status_code'] == 200:
            note.write(f"That's a good choice {st.session_state.username}, {resp['message']}")
            st.session_state.gotUsername = True  # Move to next step (set password)
            st.rerun()  # Trigger rerun to show the next step

else:
    # Show password input
    st.write(f"That's a good username {st.session_state.username}...")
    st.write("Set Your Password... And Let's Get Started...")
    passwd = st.text_input("Password", type="password")
    
    if st.button("Register"):
        # If the user is ready to register
        username = st.session_state.username
        st.write("Sending Data...", username, "", passwd)
        resp = requests.post(url="http://localhost:8000/register/", json={'username': username, 'passwd': passwd})
        resp_json = resp.json()
        
        if resp.status_code == 301 and resp_json.get('username') == st.session_state.username:
            st.success("Registration Successful")
            st.session_state.gotUsername = False  # Reset the flow for future registrations
            st.session_state.username = None  # Clear the username
        else:
            st.error("Registration Failed. Please try again.")
