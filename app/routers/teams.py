# Team-related endpoints 
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List #lets FastAPI know to expect a list; Ex: List[PlayerOut]
from .. import crud, models, schemas, database

#all routes in this file will start with /teams
router = APIRouter(prefix="/teams", tags=["players"])

# GET /teams - List all teams
@router.get("/", response_model=List[schemas.TeamOut])
def get_all_teams(db: Session = Depends(database.get_db)):
    return crud.get_teams(db)

# GET /teams/{team_id} - Get a team by ID
@router.get("/{team_id}", response_model=schemas.TeamOut)
def get_team_by_id(team_id: int, db: Session = Depends(database.get_db)):
    team = crud.get_team(db, team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team

# POST /teams - Create a new team
@router.post("/", response_model=schemas.TeamOut)
def create_team(team: schemas.TeamCreate, db: Session = Depends(database.get_db)):
    return crud.create_team(db, team)

# PUT /teams/{team_id} - Update a team
@router.put("/{team_id}", response_model=schemas.TeamOut)
def update_team(team_id: int, team: schemas.TeamCreate, db: Session = Depends(database.get_db)):
    updated_team = crud.update_team(db, team_id, team)
    if not updated_team:
        raise HTTPException(status_code=404, detail="Team not found")
    return updated_team

# DELETE /teams/{team_id} - Delete a team
@router.delete("/{team_id}", response_model=schemas.TeamOut)
def delete_team(team_id: int, db: Session = Depends(database.get_db)):
    deleted_team = crud.delete_team(db, team_id)
    if not deleted_team:
        raise HTTPException(status_code=404, detail="Team not found")
    return deleted_team






