from pydantic import BaseModel
from typing import List, Optional

#Base Schema with shared fields for a Player
#A request is compared to this model for validation
class PlayerBase(BaseModel):
    name: str
    age: int
    position: str
    player_id: int

#Schema for creating a new player (POST)
class PlayerCreate(PlayerBase):
    pass #inherits all the fields from PlayerBase

#schema for returning a player from the API (GET)
#this is the response schema that is outputted 
class PlayerOut(PlayerBase):
    id: int #return with the id

    class Config:
        # this says: "treat these SQL alchemy models like dicts"
        orm_mode = True #Enables SQLAlchemy -> Pydantic conversion

#base schema for teams
class TeamBase(BaseModel):
    name: str 
    city: str

#schema for creating a team 
class TeamCreate(TeamBase):
    pass #inherits all fields for TeamBase

class TeamOut(TeamBase):
    id: int #output with the id
    players: Optional[List[PlayerOut]] = [] #essentially tells FastAPI to expect a list of players

    class config:
        orm_mode = True


#base schema for stat
class StatBase(BaseModel):
    season: str
    games_played: int
    points_per_game: float
    rebounds_per_game: float
    assists_per_game: float

class StatCreate(StatBase):
    player_id: int #required for creating, must attach the stat to a player

class StatOut(StatBase):
    id: int

    class Config:
        orm_mode = True #SQLAlchemy objects -> JSON using these pydantic models