import streamlit as st
import streamlit.components.v1 as components
import requests

def loadCSS(filepath=""):
    with open(filepath) as file:
        st.markdown(f"<style> {file.read()} </style>", unsafe_allow_html=True)

# Load the css files
loadCSS("FrontEnd/css/style.css")

def sendCredentials(username, passwd):
    url = "http://localhost:8000/login"
    data = {
        "username": username,
        "passwd": passwd
    }
    resp = requests.post(url=url, json=data).json()
    #print(resp)
    #resp_data = resp.content.decode("utf-8").json()
    if resp['status_code'] == 301:
        st.session_state.username = ""
        st.session_state.password = ""
        st.session_state.jwt_token = resp['jwt_token']
        # Lets write the jwt-token to the client-side local storage
        #st.write("JWT-Token :", resp['jwt_token'])
        js_script = f" <script> window.localStorage.setItem('jwt_token', '{resp['jwt_token']}');</script>"
        components.html(js_script, height=0)
        st.success("LOGIN SUCCESSFUL. You may now proceed to the CHAT")
    else:
        error.error("Invalid Credentials")

st.title("Login Page")
st.session_state.username = st.text_input("Username", value=st.session_state.get('username', ''))
st.session_state.password = st.text_input("Password", type="password", value=st.session_state.get('password', ''))
error = st.empty()

if st.button("Login") and st.session_state.username != "" and st.session_state.password != "":
    sendCredentials(st.session_state.username, st.session_state.password)
