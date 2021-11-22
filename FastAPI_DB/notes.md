========================================
FastAPI Async SQL (Relational) Databases
========================================

https://pypi.org/project -- for understanding the Python packages

pip install databases
====================
Databases gives you simple asyncio support for a range of databases.
It allows you to make queries using the powerful SQLAlchemy Core expression language, and provides support for PostgreSQL, MySQL, and SQLite.
Databases is suitable for integrating against any async Web framework, such as Starlette, Sanic, Responder, Quart, aiohttp, Tornado, or FastAPI.

pip install uuid
================
UUIDs are often used as primary keys or as part of database indexes

pip install passlib
===================
Passlib is a password hashing library for Python which provides cross-platform implementations of over 30 password hashing algorithms, as well as a framework for managing existing password hashes.

pip install pydantic
=====================
Data validation and settings management using Python type hinting

pip install SQLAlchemy
======================
SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL

MetaData
=========
In SQLAlchemy. A MetaData is a container object that keeps together many different features of a database (or multiple databases) being described

pip install typing
==================
Typing defines a standard notation for Python function and variable type annotations. The notation can be used for documenting code in a concise, standard format, and it has been designed to be used by static and runtime type checkers, static analyzers, IDEs and other tools. It comes with python 3.5 and above.

pip install bcrypt
===================
Used for Good password hashing for softwares and servers

database lab
=============
Create User username with NOINHERIT LOGIN ENCRYPTED PASSWORD 'password'
Create Database databasename owner=Ownername


How to Run application
======================
uvicorn main:app --reload


** Upacking Dictionaries example
=================================
date_info = {'Year':'2021','month':'11','day':'21'}
song_info = {'artist':'Sarkodie','title':'Happy Day'}

filename_info ='{year}-{month}-{artist}-{title}.txt'.format(
    **date_info,
    **song_info,
)
filename

* Upacking List example
========================
fruits = ['lemon', 'pear', 'watermelon', 'tomato']
print(*fruits)