from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.models import Appointment
from app.schemas.schemas import AppointmentCreate, AppointmentResponse

router = APIRouter(prefix="/appointments", tags=["Appointments"])

# ✅ CREATE: Add a New Appointment
@router.post("/", response_model=AppointmentResponse)
def create_appointment(appointment: AppointmentCreate, db: Session = Depends(get_db)):
    new_appointment = Appointment(patient_id=appointment.patient_id, date_time=appointment.date_time)
    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)
    return new_appointment

# ✅ READ: Get All Appointments
@router.get("/", response_model=list[AppointmentResponse])
def get_appointments(db: Session = Depends(get_db)):
    return db.query(Appointment).all()

# ✅ READ: Get a Single Appointment by ID
@router.get("/{appointment_id}", response_model=AppointmentResponse)
def get_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment

# ✅ UPDATE: Modify an Appointment
@router.put("/{appointment_id}", response_model=AppointmentResponse)
def update_appointment(appointment_id: int, appointment_data: AppointmentCreate, db: Session = Depends(get_db)):
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    appointment.patient_id = appointment_data.patient_id
    appointment.date_time = appointment_data.date_time

    db.commit()
    db.refresh(appointment)
    return appointment

# ✅ DELETE: Remove an Appointment
@router.delete("/{appointment_id}")
def delete_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    db.delete(appointment)
    db.commit()
    return {"message": "Appointment deleted successfully"}
