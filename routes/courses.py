from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Course(BaseModel):
    name: str
    instructor: str | None = None
    credit: float = 3.0
    cost: float = 0.0

@router.post("/courses/")
async def create_course(course: Course, q: int | None = None):
    result = {"course_id": 1,
            "course_name": course.name,
            "instructor": course.instructor,
            "credit": course.credit,
            "cost": course.cost
            }
    if q:
        result.update({"semester": q})
    return result 