from typing import List
from ..models.user import User

# Mock database
users_db = [
    {
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@example.com",
        "password": "secret123"
    },
    {
        "id": 2,
        "name": "Ishika",
        "email": "abc@example.com",
        "password": "secret123"
    },
    {
        "id": 3,
        "name": "John Doe",
        "email": "123@example.com",
        "password": "secret123"
    }
]

class UserController:
    @staticmethod
    def get_users() -> List[User]:
        return users_db
    
    @staticmethod
    def get_user(user_id: int) -> User:
        return next((user for user in users_db if user.id == user_id), None)
    
    @staticmethod
    def create_user(user: User) -> User:
        users_db.append(user)
        return user 