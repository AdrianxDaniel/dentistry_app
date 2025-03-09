from fastapi import FastAPI
from app.routes import patients, appointments, auth

app = FastAPI()

app.include_router(patients.router)
app.include_router(appointments.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Dentistry App API"}
