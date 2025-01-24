from sqlalchemy import Column, Integer, Float
from .database import Base

class ObjectVariables(Base):
    __tablename__ = "object_variables"
    id = Column(Integer, primary_key=True, index=True)
    position_x = Column(Float, default=0.0)
    position_y = Column(Float, default=0.0)
    position_z = Column(Float, default=0.0)
    width = Column(Float, default=0.0)
    height = Column(Float, default=0.0)
    length = Column(Float, default=0.0)
    angle = Column(Float, default=0.0)
