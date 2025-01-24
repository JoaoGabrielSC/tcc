from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/objects/{obj_id}", response_model=schemas.ObjectVariables)
def read_object_variables(obj_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_object_variables(db, obj_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Object not found")
    return db_obj

@app.post("/objects/", response_model=schemas.ObjectVariables)
def create_object_variables(obj: schemas.ObjectVariablesCreate, db: Session = Depends(get_db)):
    return crud.create_object_variables(db, obj)

@app.put("/objects/{obj_id}", response_model=schemas.ObjectVariables)
def update_object_variables(obj_id: int, obj: schemas.ObjectVariablesUpdate, db: Session = Depends(get_db)):
    db_obj = crud.update_object_variables(db, obj_id, obj)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Object not found")
    return db_obj
