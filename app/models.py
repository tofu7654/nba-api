from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

#this file contains models of tables that will be created into tables when app runs

# Team table 
class Team(Base): #defines a class called Team. "Base" tells SQL alchemy to treat this as a model
    __tablename__ = "teams" #sets the name of the actual table to "teams" not team

    #defines a column named id with data type of integer. 
    #primary_key=True marks this column as the primary key(must be unique between teams and not NULL)
    #index=True means SQLAlchemy will create an index on column to speed up lookups
    id = Column(Integer, primary_key=True, index=True) 

    #defines a column with a string field.
    #nullable=False means that this field cannot be false - is required
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)

    #this defines a relationship to the "player" table. Says "a team has many players"
    #back_populates = "team" means the Player class must also declare a matching relationship
    #this is a one-to-many relationship (i.e one team has many players); bc there is no foreign key
    players = relationship("Player", back_populates="Team")

# Player table
class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    position = Column(String)
    #there is a foreign key here, so this is the many side
    #foreign key is used on the many side
    team_id = Column(Integer, ForeignKey("teams.id"))
    team = relationship("Team", back_populates="Player")

# Stats table
class Stat(Base):
    __tablename__ = "stats"
    id = Column(Integer, primary_key=True, index=True)
    #foreign key again so many side
    player_id = Column(Integer, ForeignKey("players.id"))
    season = Column(String)
    games_played = Column(Integer)
    points_per_game = Column(Float)
    assists_per_game = Column(Float)
    rebounds_per_game = Column(Float)
    player = relationship("Player", back_populates="stats")

#All of these tables are created when the script in Main.py is run
#Specifically the line: models.Base.metadata.create_all(bind=engine)