from fastapi import APIRouter
from sqlmodel import SQLModel, Field, Session, select
from database import engine

router = APIRouter()

class Course(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    instructor: str | None = None
    credit: float = 3.0
    cost: float = 0.0

@router.get("/courses/")
async def get_courses():
    with Session(engine) as session:
        courses = session.exec(select(Course)).all()
    return {"courses": courses}

    
@router.get("/courses/{course_id}")
async def get_course(course_id: int):
    with Session(engine) as session:
        course = session.get(Course, course_id)
    if not course:
        return {"error": "Course not found"}
    return course


@router.post("/courses/")
async def create_course(course: Course):
    with Session(engine) as session:
        session.add(course)
        session.commit()
        session.refresh(course)
    return course