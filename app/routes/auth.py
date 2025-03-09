from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login")
def login():
    return {"message": "Login route - To be implemented"}

@router.post("/register")
def register():
    return {"message": "Register route - To be implemented"}
