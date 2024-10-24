# This code will handle the logic for the Login and Register 

from fastapi import APIRouter
from variables import client
from fastapi.responses import JSONResponse
from DataModel import ResponseModel, RequestModel
from pymongo import MongoClient
from jose import JWTError, jwt
from random import randint
from time import time

login_router = APIRouter()

def generateJWTToken(username):
    payload = {
            'random-value': str(randint(1, 1000)+3600), # 
            'sub': username, 
            'exp': str(int(time())+3600)
    }
    SECRET_KEY = "IH3TeF130nt3nd"
    ALGORITHM = "HS256"

    return jwt.encode(payload, SECRET_KEY, ALGORITHM)

def validateData(name: str , passwd: str):
    """ The page is only accessible if the user is not authorized"""
    # Check if there is a account with the given credentials
    # nonlocal client
    db = client['legal-bot']; auth_collection = db['auth']
    document = db.auth.find_one({"username": name})
    if document['password'] == passwd:
        # The User is Authorized.
        return True
    else:
        return False

@login_router.post("/")
def loginUser(data: RequestModel):
    try:
        username = data.username; passwd = data.passwd
        is_valid = validateData(username, passwd)
        if is_valid:
            # Generate the JWT Token
            jwt_token = generateJWTToken(username)
            return JSONResponse(content=ResponseModel(status_code=301, message="Suceess", jwt_token=jwt_token, username=username).dict(), status_code=200)
        else:
            return JSONResponse(content=ResponseModel(status_code=404, message="Credentials Invalid", jwt_token=None, username=None).dict(), status_code=404)
    except Exception as e:
        print("Error : ", e)
        return JSONResponse(content=ResponseModel(status_code=404, message="Some Unknown Error", jwt_token=None, username=None).dict(), status_code=404)


    





