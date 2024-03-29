#!/usr/bin/python3
""" imports definition """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_state import Base, State


class City(Base):
    """ class City definition """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    states = relationship("State", back_populates="cities")
