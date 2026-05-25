from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

courses_db = []
next_id = 1

class Course(BaseModel):
    name: str
    instructor: str | None = None
    credit: float = 3.0
    cost: float = 0.0
    
@router.get("/courses/")
async def get_all_courses():
    return {"courses": courses_db}

@router.get("/courses/{course_id}")
async def get_course(course_id: int):
    for course in courses_db:
        if course["course_id"] == course_id:
            return course
    return {"error": "Course not found"}

@router.post("/courses/")
async def create_course(course: Course):
    global next_id
    result = {
        "course_id": next_id,
        "course_name": course.name,
        "instructor": course.instructor,
        "credit": course.credit,
        "cost": course.cost
        }
    courses_db.append(result)
    next_id += 1
    return result 