from fastapi import FastAPI
import uvicorn
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from argon2 import PasswordHasher
import asyncio
from argon2.exceptions import VerifyMismatchError
from pydantic import BaseModel
import os
ph = PasswordHasher()
app = FastAPI()
uri = os.getenv("MONGO_URI")

client = MongoClient(uri, server_api=ServerApi('1'))
db = client["DATABASE"]
collection = db["USERS"]

async def reset_login(username):
    await asyncio.sleep(10)

    collection.update_one(
        {"name": username},
        {"$set": {"loggingin": False}}
    )
class LoginData(BaseModel):
    username: str
    password: str
@app.get("/")
async def root():
    return {"message": "API is live",
            "success":True}


@app.post("/login")
async def login(data: LoginData):
    user = collection.find_one({"name": data.username})
    if not user:
        return {
            "success":False,
            "message":"User not found in database"
        }
    
    
    result=collection.update_one(
        {"name": data.username,
         "loggingin":False
         },
        {"$set": {"loggingin": True}})
    if result.modified_count == 0:
            return {
            "success": False,
            "message": "Please try again in a few seconds!"
        }
    asyncio.create_task(reset_login(data.username))
    try:
        ph.verify(user["password"],data.password)
        return {
                "success":True,
                "message":"Successfully logged in!"
            }
    except VerifyMismatchError:
        return {
                "success":False,
                "message":"Password is wrong!"
            }

        


