from fastapi import FastAPI
import uvicorn
from models import Base
from database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def main():
    return "Hello"

