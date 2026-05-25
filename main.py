from fastapi import FastAPI
from routes import courses
from routes import messages

app = FastAPI()
app.include_router(courses.router)
app.include_router(messages.router)