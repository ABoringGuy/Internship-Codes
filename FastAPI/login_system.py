"""response_model=Class_name, matches the return value with specified class.
It removes any extra field and gives Validation Error for missing or mismatched fields"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app=FastAPI()

class RegisterData(BaseModel):
    username: str
    password: str

class LoginData(BaseModel):
    username: str
    password: str

class UserData(BaseModel):
    id:int
    username: str
    password: str
    balance: int

user_database={}
user_id=1
@app.get("/")
def menu():
    return "Welcome to Banking System!"

@app.post("/register", response_model=UserData)
def register(user:RegisterData):
    global user_id
    new_user=UserData(id=user_id,username=user.username,password=user.password, balance=1000)
    user_database[user_id] = new_user
    user_id+=1
    return new_user


@app.post("/login")
def login(user:LoginData):
    for existing_user in user_database.values():
        if existing_user.username == user.username:
            if existing_user.password == user.password:
                return {"message":"Login Successful",
                        "username":user.username}
            raise HTTPException(status_code=401, detail="Password Incorrect. Login Unsuccessful")
    raise HTTPException(status_code=401, detail="Username Incorrect. Login Unsuccessful")

@app.get("/users")
def get_users():
    return user_database

@app.get("/users/{user_id}")
def get_user(user_id:int):
   if user_id not in user_database:
       raise HTTPException(status_code=404, detail="User Not Found")
   return user_database[user_id]

@app.put("/users/deposit/{user_id}")
def deposit(user_id:int, amount:int):
    if user_id not in user_database:
        raise HTTPException(status_code=404, detail="User Not Found")
    user_database[user_id].balance+=amount
    return user_database[user_id]

@app.put("/users/retrieval/{user_id}")
def retrieval(user_id:int, amount:int):
    if user_id not in user_database:
        raise HTTPException(status_code=404, detail="User Not Found")
    user_database[user_id].balance-=amount
    return user_database[user_id]