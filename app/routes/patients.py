from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.models import Patient
from app.schemas.schemas import PatientCreate, PatientResponse

router = APIRouter(prefix="/patients", tags=["Patients"])

# ✅ CREATE: Add a New Patient
@router.post("/", response_model=PatientResponse)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    new_patient = Patient(name=patient.name, age=patient.age, phone=patient.phone)
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient

# ✅ READ: Get All Patients
@router.get("/", response_model=list[PatientResponse])
def get_patients(db: Session = Depends(get_db)):
    return db.query(Patient).all()

# ✅ READ: Get a Single Patient by ID
@router.get("/{patient_id}", response_model=PatientResponse)
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

# ✅ UPDATE: Modify an Existing Patient
@router.put("/{patient_id}", response_model=PatientResponse)
def update_patient(patient_id: int, patient_data: PatientCreate, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    patient.name = patient_data.name
    patient.age = patient_data.age
    patient.phone = patient_data.phone
    
    db.commit()
    db.refresh(patient)
    return patient

# ✅ DELETE: Remove a Patient
@router.delete("/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    db.delete(patient)
    db.commit()
    return {"message": "Patient deleted successfully"}
