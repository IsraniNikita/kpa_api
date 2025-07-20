from fastapi import FastAPI
from app.database import Base, engine
from app.routes import form_data

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Include API routes
app.include_router(form_data.router)
