from fastapi import APIRouter, HTTPException
from ..controllers.user_controller import UserController
from ..models.user import User
from .study_plan import router as planner_router
from .auth import router as login_router

router = APIRouter()

@router.get("/users", response_model=list[User])
def get_users():
    return UserController.get_users()

@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = UserController.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users", response_model=User)
def create_user(user: User):
    return UserController.create_user(user) 

router.include_router(planner_router)
router.include_router(login_router)