from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    name: str = Field(...,min_length=3, max_length=50, description="the name of the user")
    password: str = Field(..., min_length=8, max_length=100, description="the password of the user")
    age: int = Field(...,ge=1, le=120, max_length=50, description=the age of the user)
    email: EmailStr = Field(..., format="email", description=the email of the user)

