from fastapi import FastAPI
from .routers import players, teams
from . import models, database

#This is the entry point of the FastAPI app. Include the routes.

app = FastAPI(
    title="NBA Stats API",
    description="A FastAPI app to manage NBA players, teams, and stats",
    version="1.0.0"
)

#creates the tables based on models
models.Base.metadata.create_all(bind=database.engine)

#the routers of the data types
app.include_router(players.router)
app.include_router(teams.router)