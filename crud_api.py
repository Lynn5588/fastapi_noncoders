from fastapi import FastAPI

# Initialize FastAPI app
app = FastAPI(
    title="My CRUD API",
    description="API to manage user data with POST, GET, PUT, and DELETE methods.",
    version="0.1.0",
)

from pydantic import BaseModel

# Pydantic models
class User(BaseModel):
    name: str
    email: str

@app.post("/users", tags=["User Management"])
async def create_user(user: User):
    # Create a new user
    return {"message": "User created", "user_id": 123}


# Get all users
@app.get("/users", tags=["User Management"])
async def get_all_users():
    return [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]

# Get specific user
@app.get("/users/{user_id}", tags=["User Management"])
async def get_user(user_id: int):
    return {"id": user_id, "name": "John", "email": "john@email.com"}

# Update entire user (PUT)
@app.put("/users/{user_id}", tags=["User Management"])
async def update_user(user_id: int, user: User):
    # Replace all user data
    return {"message": "User updated completely"}

# Delete a user (DELETE)
@app.delete("/users/{user_id}", tags=["User Management"])
async def delete_user(user_id: int):
    # Remove user from database
    return {"message": "User deleted"}
