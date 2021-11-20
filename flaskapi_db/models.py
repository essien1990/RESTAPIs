from enum import unique
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CarsModel(db.Model):
    __tablename__ = 'car_info'

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(64))
    model=db.Column(db.String(64))
    cylinder=db.Column(db.Integer())

    def __int__(self,name,model,cylinder):
        self.name = name
        self.model = model
        self.cylinder=cylinder

    def __repr__(self):
        return f'Car {self.name}'
    
