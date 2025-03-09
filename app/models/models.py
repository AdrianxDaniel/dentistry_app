from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database.db import Base

# ✅ Patient Model
class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    phone = Column(String, nullable=False)

    # Relationship to appointments
    appointments = relationship("Appointment", back_populates="patient")

# ✅ Appointment Model
class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    date_time = Column(DateTime, nullable=False)

    # Relationship to patients
    patient = relationship("Patient", back_populates="appointments")
