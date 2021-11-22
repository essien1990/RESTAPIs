from enum import auto
import databases, sqlalchemy, datetime, uuid
from fastapi import FastAPI
from models import UserList, UserEntry,UserUpdate,UserDelete
from typing import List
from passlib.context import CryptContext

# Handles the encryption of the password
password_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

# Postgres Database
DATABASE_URL = 'postgresql://admin:admin@localhost:5432/users'

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

# Create user_info table with column names
users = sqlalchemy.Table(

	'user_info',
	 metadata,
	 sqlalchemy.Column('id',   sqlalchemy.String, primary_key=True),
	 sqlalchemy.Column('username',   sqlalchemy.String),
	 sqlalchemy.Column('password',   sqlalchemy.String),
	 sqlalchemy.Column('firstname',   sqlalchemy.String),
	 sqlalchemy.Column('lastname',   sqlalchemy.String),
	 sqlalchemy.Column('gender',   sqlalchemy.CHAR),
	 sqlalchemy.Column('created_at',   sqlalchemy.String),
	)

engine = sqlalchemy.create_engine(
			DATABASE_URL
		)
metadata.create_all(engine)


app = FastAPI()

# event to monitor the database startup
@app.on_event("startup")
async def startup():
    await database.connect()

# event to monitor the database disconnection
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# get or fetch all Users
@app.get('/users', response_model=List[UserList])
async def get_all_users():
	query = users.select()
	return await database.fetch_all(query)


# get or fetch a User by ID
@app.get('/user/{id}', response_model=UserList)
async def get_user_by_id(id:str):
	query = users.select().where(users.c.id == id)
	return await database.fetch_one(query)


# register or create a new user 
@app.post('/users', response_model=UserList)
async def register_user(user: UserEntry):
	Uid = str(uuid.uuid4())
	Udate = str(datetime.datetime.now())
	query = users.insert().values(
		id = Uid,
		username = user.username,
		password = password_context.hash(user.password),
		firstname = user.firstname,
		lastname = user.lastname,
		gender = user.gender,
		created_at = Udate,
	)
	await database.execute(query)
	return {
		'id':Uid,
		**user.dict(),
		'created_at':Udate	
		}


# Update User
@app.put('/users', response_model=UserList)
async def update_user(user:UserUpdate):
	Udate = str(datetime.datetime.now())
	query = users.update().\
		where(users.c.id == user.id).\
			values(
				firstname = user.firstname,
				lastname = user.lastname,
				gender = user.gender,
				created_at = Udate,
			)
	await database.execute(query)

	return await get_user_by_id(user.id)


# Delete User
@app.delete('/user/{id}')
async def delete_user_by_id(user:UserDelete):
	query = users.delete().where(users.c.id== user.id)
	await database.execute(query) 

	return{
		'message':f'This user {user.id} has been deleted successfully.'
	}