from pydantic import BaseModel
from datetime import datetime

class PatientBase(BaseModel):
    name: str
    age: int
    phone: str

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int

    class Config:
        orm_mode = True

class AppointmentBase(BaseModel):
    patient_id: int
    date_time: datetime

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    id: int

    class Config:
        orm_mode = True
