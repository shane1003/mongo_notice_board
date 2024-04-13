from fastapi import APIRouter, Body, Depends, HTTPException

router = APIRouter()

@router.post("/login")
def login():
    return None