import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Country(Base):
    __tablename__ = "country"
    ID = Column(Integer, primary_key=True)
    name= Column(String(10))

class Nickname(Base):
    __tablename__ = "nickname"
    ID = Column(Integer, primary_key=True)
    nickname= Column(String(25), unique=True)

class Character(Base):
    __tablename__= "character"
    ID = Column(Integer, primary_key= True)
    pais = Column (String(20), unique=True)
    height = Column(Integer)
    mass = Column(Integer)

class Planet(Base):
    __tablename__="planet"
    ID = Column(Integer, primary_key= True)
    name = Column (String(20), unique = True)
    population = Column (Integer)
    climate = Column (String(20))
    diameter = Column (Integer)

class Vehicle(Base):
    __tablename__= "vehicle"
    ID = Column(Integer, primary_key= True)
    name = Column (String(20), unique = True)
    manufacturer = Column (String(20))
    model = Column (String(20))
    passengers = Column (Integer)

class FavoriteCharacters(Base):
    __tablename__= "favorite_characters"
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.ID"))
    character_id= Column(Integer, ForeignKey("character.ID"))

class FavoritePlanets(Base):
    __tablename__= "favorite_planets"
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.ID"))
    planet_id= Column(Integer, ForeignKey("planet.ID"))

class FavoriteVehicles(Base):
    __tablename__= "favorite_vehicles"
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.ID"))
    vehicle_id= Column(Integer, ForeignKey("vehicle.ID"))

class Favorites(Base):
    __tablename__ = "favorites"
    ID = Column(Integer, primary_key=True)
    favoritecharacter_id = Column(String(25), ForeignKey ("favorite_characters.ID"))
    ffavoritecharacter_relationship = relationship(FavoriteCharacters)
    favoritevehicle_id = Column(String(25), ForeignKey ("favorite_vehicles.ID"))
    favoritevehicle_relationship = relationship(FavoriteVehicles)
    favoriteplanet_id = Column(String(25), ForeignKey ("favorite_planets.ID") )
    favoriteplanet_relationship = relationship(FavoritePlanets)


class User(Base):
    __tablename__="user"
    ID = Column(Integer, primary_key=True)
    first_name = Column(String(20), nullable= False)
    last_name = Column(String(20), nullable= False)
    pais = Column (Integer, ForeignKey ("country.ID"))
    pais_relationship = relationship(Country)
    nickname = Column (String(25), ForeignKey ("nickname.ID"))
    nickname_relationship = relationship(Nickname)
    email = Column (String(25), unique=True)
    password = Column (String(25))
    favorite=Column(Integer, ForeignKey("favorites.ID"))
    favorite_relationship = relationship(Favorites)


# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}
       
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
