#!/usr/bin/python3
"""State model with SQLAlchemy
"""

import sys
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """State model"""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship('city', backref='states')
