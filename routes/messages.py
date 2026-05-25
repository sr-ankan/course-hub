from fastapi import APIRouter

router = APIRouter()

@router.get("/messages/")
async def get_messages(source: str = "gmail"):
    if source == "gmail":
        return {"messages": ["Message 1 from Gmail", "Message 2 from Gmail"]}
    elif source == "slack":
        return {"messages": ["Message 1 from Slack", "Message 2 from Slack"]}
    else:
        return {"messages": [], "error": f"Unknown source: {source}"}