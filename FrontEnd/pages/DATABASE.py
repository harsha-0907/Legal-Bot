# These are the various judgments form the SC and the High Court
#import pandas as pd

def loadCSS(filepath=""):
    with open(filepath) as file:
        st.markdown(f"<style> {file.read()} </style>", unsafe_allow_html=True)


loadCSS("FrontEnd/css/style.css")

data = pd.read_csv("/home/user/legal-bot-web/FrontEnd/css/urls.csv")

st.dataframe(data)
