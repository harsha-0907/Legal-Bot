# This code will handle the logic for the Login and Register 

from fastapi import APIRouter
from DataModel import ResponseModel, RequestModel
from pymongo import MongoClient
from DataModel import DB_Model
from jose import JWTError, jwt
from random import randint
from time import time

login_router = APIRouter()

def generateJWTToken(username):
    payload = {
            'random-value': str(randint(1, 1000))
            'sub': username, 
            'exp': str(time.time())
    }
    SECRET_KEY = "IH3TeF130nt3nd"
    ALGORITHM = "HS256"

    return jwt.encode(payload, SECRET_KEY, ALGORITHM)

def validateData(name: str , passwd: str):
    " The page is only accessible if the user is not authorized"
    # Check if there is a account with the given credentials
    connection_url = "mongodb+srv://root:my^7#kj@cluster0.9podb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(connection_url)
    db = client['legal-bot']; auth_collection = db['auth']
    document = auth_collection.find_one({"username": name})
    if document['password'] == passwd:
        # The User is Authorized.
        return True
    else:
        return False

@login_router.post("/")
async def loginUser(data: RequestModel):
    username = data.username; passwd = data.passwd
    is_valid = validateData(username, passwd)
    if is_valid:
        # Generate the JWT Token
        jwt_token = generateJWTToken(username)
        return ResponseModel(status_code=301, message="Suceess", jwt_token=jwt_token, username=username)
    else:
        return ResponseModel(status_code=404, message="Credentials Invalid", jwt_token=None, username=None)



    





