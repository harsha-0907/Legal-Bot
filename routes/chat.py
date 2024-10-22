# This is the chat interface end-point for the project

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from DataModel import ChatModel, Chat
from variables import client
from jose import JWTError, jwt
from time import time


#Global Variabls
context = """ 


"""
chat_router = APIRouter()
user_data = dict()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def initalizeDB():
    try:
        return client['legal-bot']['chat']
    except Exception as e:
        return None

def isConnectionValid(jwt_token):
    SECRET_KEY = "IH3TeF130nt3nd"
    ALGORITHM = "HS256"
    jwt_data = jwt.decode(jwt_token, SECRET_KEY, ALGORITHM)
    print(jwt_data)

    if int(jwt_data['exp']) > time():
        # The connection is vallid
        return username
    return False

def fetchUserHistory(username):
    global user_data
    if username in user_data:
        history = "Previous Conversations"
        for conversation in user_data[username]:
            history += f"Question: {conversation.question}\n Answer: {conversation.response}"
        return history
    else:
        user_data[username] = []
        return None

@chat_router.post("/")
def modelResponse(data: dict, jwt_token: str = Depends(oauth2_scheme)):
    try:
        username = isConnectionValid(jwt_token)
        if username:
            # Then we will obtain the data from the database
            print("Recieved a Request...")
            print(data)
            history = fetchUserHistory(username)
            if history:
                llm_query = history + ""

            return JSONResponse(content=ChatModel(chats = [], sucess=True, message="Hello", status_code=200).dict(), status_code=200)
        else:
            return JSONResponse(content=ChatModel(chats = [], sucess=True, message="Please Login First", status_code=400).dict(), status_code=404)

    except Exception as e:
        print("Error :", e)
        return JSONResponse(content=ChatModel(chats = [], sucess=False, message="Internal Error", status_code=501).dict(), status_code=501)
