# KPA Backend Assignment

## 📌 Overview
This is a backend assignment for KPA ERP, developed using **FastAPI** and **PostgreSQL**. It implements two APIs to handle basic form data submission and retrieval, following the structure provided in the Postman collection and SwaggerHub documentation.

## 🚀 Tech Stack
- Python 3.11+
- FastAPI
- SQLAlchemy
- Pydantic v2
- PostgreSQL
- Uvicorn
- Python-dotenv

## 🧩 APIs Implemented

### 1. Submit Form Data
- **Method**: `POST`
- **Endpoint**: `/form-data/submit`
- **Request Body**:
 
 
 ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "9876543210"
  }
```
- Response: 201 Created
```{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "9876543210"
}
```
### 2. Get All Submitted Form Data

- Method: GET

- Endpoint: /form-data/list

- Response:
```
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "9876543210"
  },
  ...
]
```
## ⚙️ Setup Instructions
 1. Create .env file
 ```DB_HOST=localhost
DB_PORT=5432
DB_NAME=kpa_db
DB_USER=kpa_user
DB_PASS=kpa_pass
```
2. Create Virtual Environment & Install Dependencies
```
python -m venv venv
venv\Scripts\activate   # On Windows
pip install -r requirements.txt
```

4. Run the Server
```
uvicorn app.main:app --reload
```

5. Access API Docs
```
Visit: http://127.0.0.1:8000/docs
```

## ✅ Status
 - Basic API functionality completed

 - Dockerization

 - Full API coverage from Postman collection

 - Integrated with Flutter frontend
