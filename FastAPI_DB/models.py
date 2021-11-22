from pydantic.fields import Field
import sqlalchemy
from pydantic import BaseModel

# Models
class UserList(BaseModel):
	id : str
	username: str
	password: str
	firstname: str
	lastname: str
	gender: str
	created_at: str

class UserEntry(BaseModel):
	username : str = Field(...,example='nana')
	password: str = Field(...,example='password')
	firstname: str = Field(...,example='Nana')
	lastname: str = Field(...,example='Yaw')
	gender : str =  Field(...,example='M')

class UserUpdate(BaseModel):
	id: str = Field(...,example='Enter your ID: ')
	firstname: str = Field(...,example='Nana')
	lastname: str = Field(...,example='Yaw')
	gender : str =  Field(...,example='M')

class UserDelete(BaseModel):
	id: str = Field(...,example='Enter your ID: ')