# RV Systems Private Limited — Electrical Machines Q&A Platform

A full-stack web application where authenticated users can ask questions
about electrical machines and receive AI-powered answers instantly.

## Live Demo
https://internfullstackdevelopment-production.up.railway.app

## Tech Stack
- **Backend:** Django 5.2
- **Database:** MySQL (local) / PostgreSQL (production)
- **AI Integration:** Groq API (llama-3.3-70b-versatile)
- **Frontend:** Bootstrap 5, Bootstrap Icons
- **Deployment:** Railway (Ubuntu-based Linux server)

## Features
- User registration and authentication
- Ask questions about electrical machines
- AI-generated answers stored in database
- Question history per user
- Responsive design (mobile + desktop)
- Admin panel at /admin

## Database Schema

| Table | Columns |
|-------|---------|
| auth_user | id, username, email, password, date_joined |
| qa_userprofile | id, user_id, bio, location, created_at |
| qa_question | id, user_id, question, answer, created_at |

## Local Setup

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

### 7. Seed sample data
```bash
python manage.py seed_data
```
This creates 10 users and 10 Q&A rows.
All seeded user passwords: `Test@1234`

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
sudo apt install python3-pip python3-venv nginx -y
git clone https://github.com/varunraj3011/intern_full_stack_development.git
cd intern_full_stack_development
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic
gunicorn emqna.wsgi:application --bind 0.0.0.0:8000
```

## Sample Users (after seed_data)
| Username | Password |
|----------|----------|
| alice_em | Test@1234 |
| bob_tech | Test@1234 |
| carol_eng | Test@1234 |
| david_rv | Test@1234 |
| eva_power | Test@1234 |

## API Integration
Uses Groq API with `llama-3.3-70b-versatile` model.
System prompt restricts answers to electrical machines topics only.

## Code Quality
- Follows PEP 8 standards
- All functions and classes are documented
- Environment variables used for all sensitive data
- Defensive error handling on all API calls

### 4. Configure environment variables
Create a `.env` file in the root folder:
