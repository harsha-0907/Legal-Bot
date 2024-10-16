# To implement the complete functionality of the Registering service

from fastapi import APIRouter, RedirectResponse, HTTPException, Response
from pymongo import MongoClient
from login import generateJWTToken
from DataModel import ResponseModel, RequestModel

# Initialize the Database variables
url = "mongodb+srv://root:my^7#kj@cluster0.9podb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
db_client = Mongoclient(url)
db = db_client['legal-bot']; auth_collection = db['auth']
register_route = APIRouter()

def isValidUsername(username: str):
    """ Returns True if the username exists"""
    global auth_collection
    if not auth_collection:
        return false
    resp = auth_collection.find_one({'username': username})
    if resp:
        return True
    return False

def sanitizeInput(data: RequestModel):
    # For now no sanitization
    # Here we will generally remove any smart inputs given by the user
    return data

@app.post('/check-user')
async def checkUser(data: dict):
    if isValidUsername(data['username']):
        return ResponseModel(status_code=200, username=username, message=" Lets get your Password")
    else:
        return ResponseModel(status_code=404, message = "Choose another Username")


@app.post('/')
async def registerUser(data: RequestModel):
    global auth_collection
    username, passwd = sanitizeInput(username, passwd)
    if not auth_collection:
        return ResponseModel(status_code=501, message="Internal Error")
    
    if isValidUsername(username):
        return ResponseModel(status_code=404, message="Username Already Taken")
    else:
        resp = auth_collection.insert_one({'username': username, 'password': passwd})
            return ResponseModel(status_code=301, message="Registered Successfully. please Login Now", path="/login")
        else:
            return ResponseModel(status_code=404, message="Unable to Process request now.")

