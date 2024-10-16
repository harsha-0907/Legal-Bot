# The Backend

from fastapi import FastAPI, APIRouter, Request
from starlette.middleware.base import BaseHTTPMiddleware
import login
import register


def addRoutes(app):
    app = FastAPI()
    app.include_route(login.login_router, prefix="/login")
    app.include_route(register.register_route, prefix="/register")
    return app


def initializeApp():
    app = FastAPI()
    app = addRoutes(app)
    return app

if __name__ == "__main__":
    app = initializeApp()


