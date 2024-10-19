# This is the chat interface end-point for the project

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from DataModel import ChatModel, Chat
from variables import client
from jose import JWTError, jwt
from time import time


chat_router = APIRouter()
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
        return True
    return False


@chat_router.post("/")
def modelResponse(jwt_token: str = Depends(oauth2_scheme)):
    try:
        if isConnectionValid(jwt_token):
            # Then we will obtain the data from the database
            print("Served a Request")
            return JSONResponse(content=ChatModel(chats = [], sucess=True, message="Hello", status_code=200).dict(), status_code=200)
            pass
        else:
            return JSONResponse(content=ChatModel(chats = [], sucess=True, message="Please Login First", status_code=400).dict(), status_code=404)

    except Exception as e:
        print("Error :", e)
        return JSONResponse(content=ChatModel(chats = [], sucess=False, message="Internal Error", status_code=501).dict(), status_code=501)


        
