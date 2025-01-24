from sqlalchemy import Column, Integer, Float
from .database import Base

origem: float = 0.0

class ObjectVariables(Base):
    __tablename__ = "object_variables"
    
    id = Column(Integer, primary_key=True, index=True)
    position_x = Column(Float, default=origem)
    position_y = Column(Float, default=origem)
    position_z = Column(Float, default=origem)
    width = Column(Float, default=origem)
    height = Column(Float, default=origem)
    length = Column(Float, default=origem)
    angle = Column(Float, default=origem)
