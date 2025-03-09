from pydantic import BaseModel
from datetime import datetime

# ✅ Schema for Creating a New Patient
class PatientCreate(BaseModel):
    name: str
    age: int
    phone: str

# ✅ Schema for Returning Patient Data (Includes ID)
class PatientResponse(PatientCreate):
    id: int

    class Config:
        from_attributes = True  # Pydantic v2 replacement for orm_mode

# ✅ Schema for Creating a New Appointment
class AppointmentCreate(BaseModel):
    patient_id: int
    date_time: datetime

# ✅ Schema for Returning Appointment Data (Fixing Missing 'Appointment')
class AppointmentResponse(AppointmentCreate):
    id: int

    class Config:
        from_attributes = True  # Pydantic v2 replacement for orm_mode
