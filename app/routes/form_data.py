from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.form_data import FormDataCreate, FormDataOut
from app.crud import form_data
from app.database import get_db
from typing import List

router = APIRouter()

@router.post("/formData/save", response_model=FormDataOut)
def save_form_data(data: FormDataCreate, db: Session = Depends(get_db)):
    return form_data.create_form_data(db, data)

@router.get("/formData/getFormDataByUserId/{user_id}", response_model=List[FormDataOut])
def get_form_data(user_id: int, db: Session = Depends(get_db)):
    return form_data.get_form_data_by_user_id(db, user_id)
