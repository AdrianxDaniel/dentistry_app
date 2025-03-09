from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.models import Appointment
from app.schemas.schemas import AppointmentCreate, Appointment

router = APIRouter(prefix="/appointments", tags=["Appointments"])

@router.post("/", response_model=Appointment)
def create_appointment(appointment: AppointmentCreate, db: Session = Depends(get_db)):
    db_appointment = Appointment(**appointment.dict())
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

@router.get("/", response_model=list[Appointment])
def get_appointments(db: Session = Depends(get_db)):
    return db.query(Appointment).all()
