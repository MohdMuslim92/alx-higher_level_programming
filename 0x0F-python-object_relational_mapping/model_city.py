#!/usr/bin/python3
"""
Module that contains the City class.
"""


from sqlalchemy import Column, Integer, String
from model_state import Base


class City(Base):
    """Class representing a city in the database.
    """
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForignKey('states.id'), nullable=False)
