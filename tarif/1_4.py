from fastapi import FastAPI
from schemas import UserRequest, UserResponse

app = FastAPI()

@app.get("/")
def read_root():
    return ("hello world")

@app.get("/user/{username: str}/{age:int}")
def hello_user(username: str, age: int):
    return{"hello": username , "age": age}

@app.get("/admin")
def hello_admin(username: str = None, age: int = 10):
    
    return{"hello": username , "age": age}

@app.post("/user", response_model=UserResponse)
def create_user(user: UserRequest):
    return {"message": "user created", "user": user}