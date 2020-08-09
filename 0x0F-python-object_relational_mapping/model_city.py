#!/usr/bin/python3
""" File for the City class """

from model_state import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """ City class """
    __tablename__ = 'cities'

    id = Column(
        Integer,
        nullable=False,
        autoincrement=True,
        unique=True,
        primary_key=True
    )

    name = Column(
        String(128),
        nullable=False
    )

    state_id = Column(
        Integer,
        ForeignKey("states.id"),
        nullable=False
    )
