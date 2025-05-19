# Player-related endpoints 
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/players", tag=["Players"])

#the depends(database.SessionLocal) says: "Create a new session for this request"
@router.get("/")
def get_players(db: Session = Depends(database.SessionLocal)):
    return db.query(models.Player).all()

@router.post("/")
def create_player(player: schemas.PlayerCreate, db: Session = Depends(database.SessionLocal)):
    new_player = models.Player(**player.dict())
    db.add(new_player)
    db.commit()
    db.refresh(new_player)
    return new_player