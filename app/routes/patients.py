from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.models import Patient
from app.schemas.schemas import PatientCreate, Patient

router = APIRouter(prefix="/patients", tags=["Patients"])

@router.post("/", response_model=Patient)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    db_patient = Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

@router.get("/", response_model=list[Patient])
def get_patients(db: Session = Depends(get_db)):
    return db.query(Patient).all()
