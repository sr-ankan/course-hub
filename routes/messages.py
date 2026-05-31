from fastapi import APIRouter
from sqlmodel import SQLModel, Field, Session, select
from database import engine

router = APIRouter()

class Message(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    sender: str
    recipient: str
    course_name : str
    content: str
    source: str
    
@router.get("/messages/")
async def get_all_messages():
    with Session(engine) as session:
        messages = session.exec(select(Message)).all()
    return {"messages": messages}

@router.get("/messages")
async def get_message(course_name: str, source: str | None = None):
    with Session(engine) as session:
        message = session.exec(select(Message).where(Message.course_name == course_name)).all()
        if source:
            message = [m for m in message if m.source == source]
    if not message:
        return {"error": "Message not found"}
    return message

@router.post("/messages/")
async def create_message(message: Message):
    with Session(engine) as session:
        session.add(message)
        session.commit()
        session.refresh(message)
    return message

@router.delete("/messages/{message_id}")
async def delete_message(message_id: int):
    with Session(engine) as session:
        message = session.get(Message, message_id)
        if not message:
            return {"error": "Message not found"}
        session.delete(message)
        session.commit()
    return {"message": "Message deleted successfully"}