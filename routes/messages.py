from fastapi import APIRouter
from pydantic import BaseModel 

router = APIRouter()
messages_db = []
next_id = 1

class Message(BaseModel):
    sender: str
    recipient: str
    content: str
    
@router.get("/messages/")
async def get_all_messages():
    return {"messages": messages_db}

@router.get("/messages/{message_id}")
async def get_message(message_id: int):
    for message in messages_db:
        if message["message_id"] == message_id:
            return message
    return {"error": "Message not found"}

@router.post("/messages/")
async def create_message(message: Message):
    global next_id
    result = {
        "message_id": next_id,
        "sender": message.sender,
        "recipient": message.recipient,
        "content": message.content
    }
    messages_db.append(result)
    next_id += 1
    return result