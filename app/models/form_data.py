from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class FormData(Base):
    __tablename__ = "form_data"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    name = Column(String(100))
    gender = Column(String(10))
    address = Column(Text)
