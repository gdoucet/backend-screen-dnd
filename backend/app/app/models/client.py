from atexit import register
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base



class Client(Base):
    id = Column(Integer, primary_key=True, index=True)
    register_id = Column(String, index=True)
