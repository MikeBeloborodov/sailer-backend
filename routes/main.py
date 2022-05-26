from fastapi import FastAPI, status
from schemas.message import Message
from fastapi.middleware.cors import CORSMiddleware
import routes.users
from database.database_logic import Base, engine

# sqalchemy creates tables
# Base.metadata.create_all(bind=engine)


app = FastAPI()

# if you want only specific servers to be able to talk to your api
# put them in origins, otherwise use "*" to allow everyone
# origins = ["http://www.google.com"]
origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# main page
@app.get("/", status_code=status.HTTP_200_OK, response_model=Message)
def root() -> Message:
    return Message(message="Welcome to Sailer API.")


# router for users
app.include_router(routes.users.router)