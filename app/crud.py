# This file handles database logic like creating, read, updating, deleting
# Put all of the database logic here to have modularity and seperation of concerns

from sqlalchemy.orm import Session 
from . import models, schemas

#Create a player
#accepts an active SQLAlchemy session and a pydantic object containing the player data
def create_player(db: Session, player: schemas.PlayerCreate):
    new_player = models.Player(**player.model_dump()) #first turn the pydantic object into a dict and turn that into a SQLAlchemy Player object
    db.add(new_player) #stage the new player to be added to DB
    db.commit() #write changes to the database
    db.refresh(new_player) #reload the player_object from the database; now any auto-generated values are filled
    return new_player #return that new_player object

#Accepts an active session and returns a list of all the players
def get_players(db:Session):
    return db.query(models.Player).all()

#accepts a session and player_id; filters the players table and finds the first player with a matching id
def get_player(db: Session, player_id: int):
    return db.query(models.Player).filter(models.Player.id == player_id).first()

def update_player(db: Session, player_id: int, updated_data: schemas.PlayerCreate):
    #retrieve the SQLAlchemy player object 
    player = get_player(db, player_id)
    if not player:
        return None
    
    #updates the fields of the player
    for key, value in updated_data.model_dump.items():
        setattr(player, key, value)
    
    db.commit()
    db.refresh(player) #reloads the latest DB state into python object
    return player
    
def delete_player(db: Session, player_id: int):
    #retrieve player
    player = get_player(db, player_id)
    if not player:
        return None
    db.delete(player)
    db.commit()
    return player

# Team CRUD Functions

#create team
def create_team(db: Session, team: schemas.TeamCreate):
    new_team = models.Team(**team.model_dump)
    db.add(new_team)
    db.commit()
    db.refresh(new_team)
    return new_team


#This function reads all the teams
def get_teams(db: Session):
    return db.query(models.Team).all()

#this function reads a team by a given id
def get_team(db: Session, team_id: int):
    return db.query(models.Team).filter(models.Team == team_id).first()

def update_team(db: Session, team_id: int, updated_team: schemas.PlayerCreate):
    team = get_team(db, team_id)
    if not team:
        return None
    
    #updates the fields of the team
    for key, value in updated_team.model_dump.items():
        setattr(team, key, value)
    
    db.commit()
    db.refresh(team) #reloads the latest DB state into python object
    return team

def delete_team(db: Session, team_id: int):
    #first get the team and see if it exists 
    team = get_team(db, team_id)
    if not team:
        return None
    db.delete(team)
    db.commit()
    return team



