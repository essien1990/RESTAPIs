from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

user_db = []

# users model -- fake database to store users
class User(BaseModel):
    id:int
    first_name:str
    last_name:str
    email:str
    created_at:datetime = datetime.now()

# Create users
@app.post('/users')
async def create_users(users: User):
   user_db.append(users.dict())
   user_db[-1]
   return {'message':f'User {users.first_name} is created successfully'}


# get all users
@app.get("/users", response_model=list[User])
async def get_users():
    return user_db


# Get by id
@app.get("/user/{id}")
async def get_user(id: int):
    try:
        user = id
        return user_db[user]
    except:
        raise HTTPException(status_code=404, detail='User not found...!')

# Update user
@app.put('/user/{id}')
async def update_user(id: int, user:User):
    try:
        user_db[id] = user
        return {'message':f'User {user.first_name} has been updated successfully'}
    except:
        raise HTTPException(status_code=404, detail='User not found...!')

# delete User
@app.delete('/user/{id}')
async def delete_user(id: int, user:User):
    try:
        user_db.pop(id)
        return {'message':f'User {user.first_name} has been deleted successfully'}
    except:
        raise HTTPException(status_code=404, detail='User not found...!')

