# To implement the complete functionality of the Registering service

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from variables import client
from pymongo import MongoClient
from routes.login import generateJWTToken
from DataModel import ResponseModel, RequestModel

# Initialize the Database variables
url = "URL"
db_client = MongoClient(url)
db = db_client['legal-bot']; auth_collection = db['auth']

register_route = APIRouter()

def isValidUsername(username: str):
    """ Returns True if the username exists"""
    global auth_collection
    if 'auth' not in db.list_collection_names():
        return False
    else:
        resp = auth_collection.find_one({'username': username})
        if resp:
            return True
        return False

def sanitizeInput(data: RequestModel):
    # For now no sanitization
    # Here we will generally remove any smart inputs given by the user
    return data

@register_route.post('/check-user')
def checkUser(data: dict):
    username = data['username']
    if not isValidUsername(username):
        return JSONResponse(content=ResponseModel(status_code=200, username=username, message=" Lets get your Password").dict(), status_code=200)
    else:
        return JSONResponse(content=ResponseModel(status_code=404, message = "Choose another Username").dict(), status_code = 200)

@register_route.post('/')
def registerUser(data: RequestModel):
    global auth_collection
    data = sanitizeInput(data)
    username = data.username; passwd = data.passwd
    if 'auth' not in db.list_collection_names():
        return JSONResponse(content=ResponseModel(status_code=501, message="Internal Error").dict(), status_code=501)
    
    if isValidUsername(username):
        return JSONResponse(content=ResponseModel(status_code=404, message="Username Already Taken").dict(), status_code=404)
    else:
        resp = auth_collection.insert_one({'username': username, 'password': passwd})
        if resp:
            return JSONResponse(content=ResponseModel(status_code=301, message="Registered Successfully. please Login Now", path="/login", username= username).dict(), status_code=301)
        else:
            return JSONResponse(content=ResponseModel(status_code=404, message="Unable to Process request now.").dict(), status_code=404)

