from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI app
app = FastAPI(
    title="Student Management API (In-Memory)",
    description="A simple API to manage student data CRUD operations using an in-memory list.",
    version="0.1.0",
)

# Data model
class User(BaseModel):
    name: str
    age: int
    grade: float

class UserUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    grade: Optional[float] = None

# Fake database
users_db = []
next_id = 1

# CREATE - POST method
@app.post("/student_list", tags=["Register"])
async def create_user(user: User):
    global next_id
    new_user = {
        "ID": next_id,
        "Student Name": user.name,
        "Age (Year)": user.age,
        "Grade (Last Year CGPA)": user.grade
    }
    users_db.append(new_user)
    next_id += 1
    return {"message": "New Student Registered", "student": new_user}


# READ - GET methods
@app.get("/student_list", tags=["Read"])
async def get_all_users():
    return {"Student Name": users_db}

@app.get("/student_list/{user_id}", tags=["Read"])
async def get_user(user_id: int):
    for user in users_db:
        if user["ID"] == user_id:
            return {"Student Name": user}
    return {"error": "Student name not found"}


# UPDATE - PUT method (complete update)
@app.put("/student_list/{user_id}", tags=["Update"])
async def update_user(user_id: int, user_updates: UserUpdate):
    for i, user in enumerate(users_db):
        if user["ID"] == user_id:
            # Only update fields that are provided
            if user_updates.name is not None:
                users_db[i]["Student Name"] = user_updates.name
            if user_updates.age is not None:
                users_db[i]["Age (Year)"] = user_updates.age
            if user_updates.grade is not None:
                users_db[i]["Grade (Last Year CGPA)"] = user_updates.grade
            return {"message": "Student's Data Updated", "Student Name": users_db[i]}
    return {"error": "Student data not found"}


# DELETE - DELETE method
@app.delete("/student_list/{user_id}", tags=["Delete"])
async def delete_user(user_id: int):
    for i, user in enumerate(users_db):
        if user["ID"] == user_id:
            deleted_user = users_db.pop(i)
            return {"Message": "Student eliminated!", "Student Name": deleted_user}
    return {"error": "Student data not found"}

