# The Server Logic

# Import all the necessary packages
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def getMainPage():
    return {"msg": "Welcome to the Server"}