from pydantic import BaseModel
from typing import List, Dict
from datetime import date

class SubjectInput(BaseModel):
    name: str
    exam_date: date
    total_hours: int

class PlannerRequest(BaseModel):
    subjects: List[SubjectInput]
    available_hours_per_day: int

class StudyPlanDay(BaseModel):
    date: date
    subjects: Dict[str, int]  # subject -> hours

class PlannerResponse(BaseModel):
    user_id: int
    timetable: List[StudyPlanDay]
