# app/controllers/logout_controller.py

from ..models.api_response import ApiResponse

class LogoutController:
    @staticmethod
    def logout() -> ApiResponse:
        return ApiResponse.create(200, None, "Logout successful")
