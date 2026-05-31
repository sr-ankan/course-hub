from fastapi import FastAPI
from routes import courses
from routes import messages
from database import create_db_and_tables

app = FastAPI()
app.include_router(courses.router)
app.include_router(messages.router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()