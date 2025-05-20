# nba-api

## Database Notes

Database Schema - a blueprint for the database; tells PostgreSQL the following:

* what tables and columns exist
* what *type* of data is in each column
* how tables *relate* to each other

FastAPI uses SQLAlchemy to define the schema in python code, not raw SQL

Ex: Models.py

### SQL Alchemy

* Sessions - Essentially a workspace for talking to the database; like opening a document, editing it, saving it and closing
  * When a request comes in, you create a **session** this session is used to query, add, update, or delete data
  * you commit changes if needed and **close** the session when request is done; resources 

Imports:

* create_engine - SQLAlchemy function that connects to the actual database; manages connections and issues SQL commands to the DB

### Pydantic - data validation and settings management library

* used for validating data (right type/format)
  * request validation - in FastAPI, makes sure a request is in the right format; would throw an error
* parse data (convert JSON, dicts, etc to Python objects)
* serialize data (convert python objects to JSON responses)

### Routers Directory

Contains all the API Endppoints related to data. i.e getting, creating, updating, or deleting players.

