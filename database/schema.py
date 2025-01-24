from pydantic import BaseModel

class ObjectVariablesBase(BaseModel):
    position_x: float
    position_y: float
    position_z: float
    width: float
    height: float
    length: float
    angle: float

class ObjectVariablesCreate(ObjectVariablesBase):
    pass

class ObjectVariablesUpdate(ObjectVariablesBase):
    pass

class ObjectVariables(ObjectVariablesBase):
    id: int

    class Config:
        orm_mode = True
