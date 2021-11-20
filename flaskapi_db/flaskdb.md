pyscopg2, which is the PostgreSQL database adapter for Python

SQLAlchemy: is an ORM(Objects relational model) written in Python to give developers the power and flexibility of SQL, without the hassle of really using it. It gives away around to interact with the Databases without using SQL statements.

Unlink Django, that has an inbuilt ORM which comes with a pre-built ORM in the form of Django Models. Flask does not have that why Flask-SQLAlchemy ORM library is installed to use for the models.

Flask-Migrate, uses Alembic which is a light Database migration tool. It helps us to Create/Update Databases and Tables. It also allows us to update an existing Table incase you delete or create new Table Fields.

Alembic is a lightweight database migration tool for usage with the SQLAlchemy Database Toolkit for Python


pip install psycopg2-binary
pip install flask-sqlalchemy
pip install Flask-Migrate

<!-- Create Database called cars -->
create the Models for Cars

--Create a model
A Model is a Python Class that represents a table in the Database.

--Interact with the Table like a class object
    -db.session.add() to add new data
    -db.session.comit() to save the changes


--Connect Postgres to the Flask Application
    -We create a Flask object – app
    -Configure the PostgreSQL Connection
    -Keep SQL_TRACK_MODIFICATIONS to False just for simplicity.
    -Pass on app object to the SQLAlchemy object db
    -Create a Migrate Object for migrations.

<!-- RUN flask DB init -->
--flask db init
Creating directory /Volumes/MacBackup/flaskapidb/migrations ...  done
Creating directory /Volumes/MacBackup/flaskapidb/migrations/versions ...  done
Generating /Volumes/MacBackup/flaskapidb/migrations/script.py.mako ...  done
Generating /Volumes/MacBackup/flaskapidb/migrations/env.py ...  done
Generating /Volumes/MacBackup/flaskapidb/migrations/README ...  done
Generating /Volumes/MacBackup/flaskapidb/migrations/alembic.ini ...  done
Please edit configuration/connection/logging settings in
'/Volumes/MacBackup/flaskapidb/migrations/alembic.ini' before proceeding.

<!-- Run FLask DB migrate -->
flask db migrate
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'car_info'
Generating /Volumes/MacBackup/flaskapidb/migrations/versions/5133b7a409cf_.py ...  done

  <!-- RUN flask db upgrade -->
---flask db upgrade
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 5133b7a409cf, empty message


All classes have a function called __init__(), which is always executed when the class is being initiated
The __int__() function is used to assign values to object properties, or other operations that are necessary to do when the object is being created.

The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class

__repr__ is a special method used to represent a class's objects as a string.

example:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

