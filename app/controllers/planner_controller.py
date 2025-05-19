from datetime import date, timedelta
from collections import defaultdict
from ..models.study_planner import  PlannerRequest, PlannerResponse, StudyPlanDay

class PlannerController:
    @staticmethod
    def generate_timetable(user_id: int, request: PlannerRequest) -> PlannerResponse:
        today = date.today()
        timetable = defaultdict(lambda: defaultdict(int))

        for subject in sorted(request.subjects, key=lambda s: s.exam_date):
            days_left = (subject.exam_date - today).days
            if days_left <= 0:
                continue

            daily_hours = max(subject.total_hours // days_left, 1)

            for i in range(days_left):
                study_date = today + timedelta(days=i)
                current_hours = sum(timetable[study_date].values())
                if current_hours + daily_hours <= request.available_hours_per_day:
                    timetable[study_date][subject.name] += daily_hours
                else:
                    remaining = request.available_hours_per_day - current_hours
                    if remaining > 0:
                        timetable[study_date][subject.name] += remaining

        plan = [
            StudyPlanDay(date=dt, subjects=dict(hours))
            for dt, hours in sorted(timetable.items())
        ]

        return PlannerResponse(user_id=user_id, timetable=plan)
