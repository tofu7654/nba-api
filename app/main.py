from fastapi import FastAPI
from .routers import players, teams
from . import models, database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

app.include_router(players.router)
app.include_router(teams.router)