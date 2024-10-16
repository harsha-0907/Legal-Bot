# The Backend Server

from fastapi import FastAPI
from routes.login import login_router  # Assuming login_router is defined in routes/login.py
from routes.register import register_route  # Assuming register_route is defined in routes/register.py

# Function to add routes to the app
def addRoutes(app: FastAPI):
    app.include_router(login_router, prefix="/login")
    app.include_router(register_route, prefix="/register")
    return app

# Initialize the app with routes
app = FastAPI()  # Create the FastAPI instance
app = addRoutes(app)  # Add routes to the app

if __name__ == "__main__":
    os.system("streamlit run FrontEnd/HOME.py &")