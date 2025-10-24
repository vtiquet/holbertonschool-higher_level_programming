#!/usr/bin/python3
"""
Defines the City model, which links to the MySQL table cities.
It includes a ForeignKey relationship to the State model.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """
    Represents a city for a MySQL database using SQLAlchemy ORM.

    Attributes:
        __tablename__ (str): The table name.
        id (sqlalchemy.Integer): The city's unique identifier (Primary Key).
        name (sqlalchemy.String): The city's name.
        state_id (sqlalchemy.Integer): The foreign key linking to states.id.
    """
    __tablename__ = 'cities'
    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      nullable=False)
