# Player-related endpoints 
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List #lets FastAPI know to expect a list; Ex: List[PlayerOut]
from .. import crud, models, schemas, database

#all routes in this file will start with /players; tags=["Players"] groups these endpoints in Swagger UI
router = APIRouter(prefix="/players", tags=["Players"])

#the depends(database.get_db) says: "Create a new session for this request"
# a get request to /players; creates a session called db and queries all players from the database
# converts all of them to JSON
@router.get("/", response_model=List[schemas.PlayerOut])
def read_players(db: Session = Depends(database.get_db)):
    return crud.get_players(db)

#a get request to /players/1 will return the player with the id 1 as a SQLAlchemy object
@router.get("/{player_id}", response_model=schemas.PlayerOut)
def read_player(player_id: int, db: Session = Depends(database.get_db)): #player id is at front because it is non-default
    player = crud.get_player(db, player_id) 
    if not player:
        return None
    return player

#POST request to /players; returns newly created player (PlayerOut)
# must match the PlayerCreate Schema and accepts the player object from the request and db session
@router.post("/", response_model=schemas.PlayerOut)
def create_player(player: schemas.PlayerCreate, db: Session = Depends(database.get_db)):
    crud.create_player(db, player)

@router.put("/{player_id}", response_model=schemas.PlayerOut)
def updated_player(player_id: int, player: schemas.PlayerCreate, db: Session = Depends(database.get_db)):
    updated_player = crud.update_player(db, player_id, player)
    if not updated_player:
        raise HTTPException(status_code=404, detail="Player not found")
    return updated_player

#Delete player
@router.delete("/{player_id}", response_model=schemas.PlayerOut)
def delete_player(player_id: int, db: Session = Depends(database.get_db)):
    deleted = crud.delete_player(player_id, db)
    if not deleted: 
        raise HTTPException(status_code=404, detail="Player not found")
    return deleted


    