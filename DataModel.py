# The model for various parts of the code

from pydantic import BaseModel
from typing import Optional

class ResponseModel(BaseModel):
    status_code: Optional[int] = 401
    port: Optional[int] = None
    path: Optional[str] = None
    username: Optional[str] = None
    jwt_token: Optional[str] = None
    message: Optional[str] = ""

class RequestModel(BaseModel):
    username: str
    passwd: str
