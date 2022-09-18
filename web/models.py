from sqlalchemy import Column, Integer, String , ForeignKey
from .database import Base



class Cotigory(Base):
    __tablename__ = 'cotigors'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    status = False
    description = Column(String)

class SubCotigory(Base):
     __tablename__ = 'subcotigors'
     id = Column(Integer, primary_key=True, index=True)
     description = Column(String)
     cotigory_id = Column(Integer , ForeignKey("cotigors.id"))
     status = False
