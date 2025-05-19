from fastapi import APIRouter
from ..models.study_planner  import PlannerRequest, PlannerResponse
from app.controllers.planner_controller import PlannerController

router = APIRouter()

@router.post("/users/{user_id}/study-plan", response_model=PlannerResponse)
def create_study_plan(user_id: int, request: PlannerRequest):
    print(f"Received user_id: {user_id}")
    print(f"Received request: {request}")
    return PlannerController.generate_timetable(user_id, request)
