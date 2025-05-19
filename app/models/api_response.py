# app/models/api_response.py
from pydantic import BaseModel
from typing import Any

class ApiResponse(BaseModel):
    status_code: int
    data: Any
    message: str = "Success"
    success: bool = True

    @classmethod
    def create(cls, status_code: int, data: Any, message: str = "Success"):
        return cls(
            status_code=status_code,
            data=data,
            message=message,
            success=status_code < 400
        )
