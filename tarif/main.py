from fastapi import FastAPI, status, HTTPException
from schemas import UserRequest, UserResponse, UserOutput
from typing import List

app = FastAPI()
users = []

@app.get("/")
def read_root():
    return ("hello world")

@app.get("/user/{username}/{age}")
def hello_user(username: str, age: int):
    return{"hello": username , "age": age}

@app.get("/admin")
def hello_admin(username: str = None, age: int = 10):
    
    return{"hello": username , "age": age}

@app.post("/user", response_model=UserResponse, status_code=status.HTTP_201_CREATED)#میتونی 201 خالی هم بزنی ولی این بهتره
def create_user(user: UserRequest):
    # for u in users:
    #     if u.email == user.email:
    #         raise HTTPException(
    #             status_code=status.HTTP_400_BAD_REQUEST,
    #             detail="Email alreadi exists")

    #بالایی هم میشه ولی پایینی حرفه ای تره
    if any(u.email == user.email for u in users):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )
    

    new_user = UserOutput(
    id= len(users) + 1,
    # name=user.name,
    # age=user.age,
    # email=user.email
#بالایی تبدیل کردیم به پایینی
    **user.model_dump()
    )
    users.append(new_user)
    return {"message": "user created", "user": new_user}



@app.get("/users", response_model=list[UserOutput])
def get_users():
    return users

@app.get("/user/{user_id}", response_model=UserOutput)
def get_user(user_id:int):
    #next فرقش با any  اینه که خود user v رو برمیگردونه
    user = next((u for u in users if u.id == user_id), None)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user
    
    #بدون next اینجوریه:

    # user = None
    # for u in users:
    #     if u.id == user_id:
    #         user = u 
    #         break
