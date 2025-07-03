# Fitness_Booking_app
A simple RESTful Booking API built with Django and Django REST Framework for a fictional fitness studio offering Yoga, Zumba, and HIIT classes.

# Features

- View available fitness classes
- Book a class (with slot availability check)
- View all bookings by email
- Timezone conversion support (default IST, user can set via query param)
- SQLite in-memory DB (easy setup)
- Clean and modular code
- Manual seeding via script (`seed.py`)

# Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework
- SQLite (default Django DB)
- Timezone support via `pytz`

# Setup Instructions

# 1. Clone the Repository

```bash
git clone https://github.com/your-username/fitness-booking-api.git
cd fitness-booking-api
```

# 2. Create Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# 3. Install Dependencies

pip install -r requirements.txt

# 4. Run Migrations

python manage.py migrate

# 5.  Seed Sample Data

python seed.py

This command will insert the data into the database.

# 6. Run the Server

python manage.py runserver

# 7. Sample CURL Commands

### 1. Book a Class: 
curl -X POST http://127.0.0.1:8000/book/ \-H "Content-Type: application/json" \ -d "{\"class_id\": 1, \"client_name\": \"Arjun\", \"client_email\": \"arjun@example.com\"}"

### 2. View Bookings:
curl http://127.0.0.1:8000/bookings/?email=arjun@example.com

### 3. View Classes:
curl http://127.0.0.1:8000/classes/?tz=Asia/Kolkata

### 4. View Classes in EST:

curl http://127.0.0.1:8000/classes/?tz=America/New_York
