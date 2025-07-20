from pydantic import BaseModel, ConfigDict

class FormDataCreate(BaseModel):
    name: str
    email: str
    phone: str

class FormDataOut(FormDataCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
