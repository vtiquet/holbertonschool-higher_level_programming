#!/usr/bin/python3
"""
Defines the State model, which links to the MySQL table states.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for declarative class definitions
Base = declarative_base()


class State(Base):
    """
    Represents a state for a MySQL database.

    Attributes:
        __tablename__ (str): The table name.
        id (sqlalchemy.Integer): The state's id.
        name (sqlalchemy.String): The state's name.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        """Returns a string representation of the State object."""
        return "<State(id='%s', name='%s')>" % (self.id, self.name)
