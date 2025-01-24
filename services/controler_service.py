from sqlalchemy.orm import Session
from database import models, schema

class ControllerService:

    def __init__(self):
        pass

    def get_object_variables(self, db: Session, obj_id: int):
        return db.query(models.ObjectVariables).filter(models.ObjectVariables.id == obj_id).first()

    def create_object_variables(self, db: Session, obj: schema.ObjectVariablesCreate):
        db_obj = models.ObjectVariables(**obj.model_dump())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update_object_variables(self, db: Session, obj_id: int, obj: schema.ObjectVariablesUpdate):
        db_obj = self.get_object_variables(db, obj_id)
        if db_obj:
            for key, value in obj.dict().items():
                setattr(db_obj, key, value)
            db.commit()
            db.refresh(db_obj)
        return db_obj
