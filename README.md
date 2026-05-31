# RV Systems Private Limited — Electrical Machines Q&A Platform

A Django web application where authenticated users can ask questions about
electrical machines and receive AI-powered answers via Groq API.

## Tech Stack
- Backend: Django 5.2
- Database: MySQL (local) / SQLite (production)
- AI: Groq API (llama-3.3-70b-versatile)
- Frontend: Bootstrap 5

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/varunraj3011/intern_full_stack_development.git
cd intern_full_stack_development
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Copy `.env.example` to `.env` and fill in your values:

SECRET_KEY=your-secret-key
DEBUG=True
GROQ_API_KEY=your-groq-api-key
USE_MYSQL=True
DB_NAME=emqna_db
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306


### 5. Create MySQL database
```sql
CREATE DATABASE emqna_db CHARACTER SET utf8mb4;
```

### 6. Run migrations
```bash
python manage.py migrate
```

### 7. Seed sample data (10 users + 10 Q&A rows)
```bash
python manage.py seed_data
```

### 8. Create admin user
```bash
python manage.py createsuperuser
```

### 9. Run the server
```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000

## Ubuntu Server Deployment

```bash
sudo apt update
sudo apt install python3-pip python3-venv nginx mysql-server -y
git clone <your-repo-url>
cd intern_full_stack_development
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn
python manage.py migrate
python manage.py collectstatic
gunicorn emqna.wsgi:application --bind 0.0.0.0:8000
```

## Features
- User registration and login
- Ask questions about electrical machines
- AI-generated answers stored in MySQL
- Question history per user
- Admin panel at /admin
- Responsive design (mobile + desktop)

## Database Schema
| Table | Columns |
|-------|---------|
| auth_user | id, username, email, password, date_joined |
| qa_userprofile | id, user_id, bio, location, created_at |
| qa_question | id, user_id, question, answer, created_at |

## Sample Users (after seed_data)
All passwords: `Test@1234`
Users: alice_em, bob_tech, carol_eng, david_rv, eva_power...

## Admin Access
URL: /admin  
Create with: `python manage.py createsuperuser`
