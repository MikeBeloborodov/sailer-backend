from fastapi import FastAPI, status
from schemas.message import Message

app = FastAPI()

@app.get("/", status_code=status.HTTP_200_OK, response_model=Message)
def root() -> Message:
    return Message(message="Welcome to Sailer API.")