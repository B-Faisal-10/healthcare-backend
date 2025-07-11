# 🏥 Django Healthcare Backend API

This project is a secure and robust healthcare backend system built with Django, Django REST Framework (DRF), PostgreSQL, and JWT Authentication.

---

## 🚀 Features

- 🔐 User Registration and Login using JWT
- 🧑‍⚕️ Add & Manage Patients and Doctors
- 🔄 Assign Doctors to Patients
- ✅ RESTful API Endpoints
- 🔐 JWT-secured APIs (using `djangorestframework-simplejwt`)
- 🔄 PostgreSQL database integration

---

## 🛠️ Tech Stack

- Django 4+
- Django REST Framework
- PostgreSQL
- JWT Authentication (via `simplejwt`)
- Python Decouple (.env support)

---

## 📦 Installation

### 1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/healthcare-backend.git
cd healthcare-backend

### 2. Create and Activate Virtual Environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Setup PostgreSQL Database
Create a PostgreSQL database and user, then configure the .env file.

🔐 Sample .env.example

DB_NAME=db_healthcare
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your_django_secret_key
Do not commit your actual .env file. Keep it secret!

🗃️ Migrate & Run the Server

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

🔐 Authentication

POST /api/auth/register/ — Register new user

POST /api/auth/login/ — Get JWT access + refresh token

👤 Patient Management

POST /api/patients/ — Create patient

GET /api/patients/ — List patients

GET /api/patients/<id>/ — Retrieve patient

PUT /api/patients/<id>/ — Update patient

DELETE /api/patients/<id>/ — Delete patient

🧑‍⚕️ Doctor Management

POST /api/doctors/ — Create doctor

GET /api/doctors/ — List doctors

GET /api/doctors/<id>/ — Retrieve doctor

PUT /api/doctors/<id>/ — Update doctor

DELETE /api/doctors/<id>/ — Delete doctor

🔁 Patient-Doctor Mapping

POST /api/mappings/ — Assign doctor to patient

GET /api/mappings/ — All mappings

GET /api/mappings/<patient_id>/ — Doctors for patient

DELETE /api/mappings/<id>/ — Remove doctor from patient


👨‍💻 Author
Faisal Badane
https://github.com/B-Faisal-10/
GitHub
