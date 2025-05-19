
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..controllers.login_controller import LoginController
from ..controllers.logout_controller import LogoutController
from ..models.user import User
from ..models.api_response import ApiResponse


router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login", response_model=ApiResponse)
def login(login_request: LoginRequest):
    print("Received LoginRequest:", login_request)
    return LoginController.login(login_request.email, login_request.password)


@router.post("/logout", response_model=ApiResponse)
def logout():
    return LogoutController.logout()