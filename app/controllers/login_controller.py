# app/controllers/login_controller.py
from fastapi import HTTPException
from ..models.user import User
from ..models.api_response import ApiResponse
from .user_controller import users_db  # Mock DB

class LoginController:
    @staticmethod
    def login(email: str, password: str) -> ApiResponse:
        user = next((user for user in users_db if user["email"] == email and user["password"] == password), None)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid email or password")
        
        user_obj = User(id=user["id"], name=user["name"], email=user["email"], password=user.get("password"))
        return ApiResponse.create(200, user_obj.dict(exclude={"password"}), "Login successful")

