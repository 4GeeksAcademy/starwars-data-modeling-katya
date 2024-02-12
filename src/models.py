import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(100))
    password = Column(String(128))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    climate = Column(Enum('desert', 'grasslands, mountains', 'jungle, rainforests', 'tundra, ice caves, mountain ranges', 'swamp, jungles'))
    population = Column(Integer)
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)
    diameter = Column(Integer)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    gender = Column(Enum('female', 'male', 'other', 'n/a'))
    birth_year = Column(Integer)
    height = Column(Integer)
    hair_color = Column(Enum('brown', 'blond', 'red', 'black', 'n/a'))
    eye_color = Column(Enum('brown', 'green', 'blue', 'gold', 'n/a'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    model = Column(String(100))
    vehicle_class = Column(Enum('repulsorcraft', 'wheeled', 'starfighter'))
    manufacturer = Column(Enum('Incom Corporation', 'Corellia Mining Corporation'))
    length = Column(Integer)
    passengers = Column(Integer)
    pilot_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    user = relationship(User)
    character = relationship(Character)
    planet = relationship(Planet)
    vehicle = relationship(Vehicle)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
