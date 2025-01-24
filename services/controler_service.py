from sqlalchemy.orm import Session
from . import models, schemas

class ControllerService:

    def get_object_variables(db: Session, obj_id: int):
        return db.query(models.ObjectVariables).filter(models.ObjectVariables.id == obj_id).first()

    def create_object_variables(db: Session, obj: schemas.ObjectVariablesCreate):
        db_obj = models.ObjectVariables(**obj.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update_object_variables(self, db: Session, obj_id: int, obj: schemas.ObjectVariablesUpdate):
        db_obj = self.get_object_variables(db, obj_id)
        if db_obj:
            for key, value in obj.dict().items():
                setattr(db_obj, key, value)
            db.commit()
            db.refresh(db_obj)
        return db_obj
