from sqlalchemy.orm import Session
from app.models.form_data import FormData
from app.schemas.form_data import FormDataCreate

def create_form_data(db: Session, form_data: FormDataCreate):
    db_obj = FormData(**form_data.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_form_data_by_user_id(db: Session, user_id: int):
    return db.query(FormData).filter(FormData.user_id == user_id).all()
