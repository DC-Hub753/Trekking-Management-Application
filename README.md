# Trekking Management Application

A role-based trekking management web application built with **Flask, Python, SQLAlchemy, and SQLite**. The application supports trek management, staff assignments, user registration, and booking management through separate role-based dashboards.

**Live Website:** https://trekking-management-application-sjfe.onrender.com/

## Features

- **Admin Dashboard** — View users, staff, treks, and bookings.
- **Trek Management** — Add, view, edit, and delete treks.
- **Staff Management** — Review staff registrations, approve staff, assign treks, and manage staff access.
- **User Management** — View users and manage blacklisted accounts.
- **User Registration & Login** — Register and securely authenticate users.
- **Staff Registration & Login** — Staff registration with admin approval.
- **Booking Management** — View and manage trekking bookings.
- **Role-Based Access Control** — Separate permissions for admins, staff, and users.
- **Password Hashing** — Store passwords as hashes rather than plain text.

## Tech Stack

| Component | Technology |
|---|---|
| Backend | Python, Flask |
| Database | SQLite |
| ORM | Flask-SQLAlchemy |
| Authentication | Flask-Login |
| Password Security | Werkzeug |
| Frontend | HTML, CSS, Jinja2 templates |
| Production Server | Gunicorn |
| Deployment | Render |
| Version Control | Git and GitHub |

## Project Structure

```text
Trekking-Management-Application/
├── app.py
├── config.py
├── models.py
├── requirements.txt
├── routes/
│   ├── auth.py
│   ├── admin.py
│   ├── staff.py
│   └── user.py
├── templates/
│   ├── admin/
│   ├── staff/
│   └── user/
└── instance/
```

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/DC-Hub753/Trekking-Management-Application.git
cd Trekking-Management-Application
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Windows PowerShell:

```powershell
$env:SECRET_KEY = "your_generated_secret_key"
$env:ADMIN_USERNAME = "your_admin_username"
$env:ADMIN_PASSWORD = "your_strong_admin_password"
```

Use a strong, unique secret key and admin password. Do not commit real secrets to GitHub.

### 5. Start the application

```bash
python app.py
```

Open http://127.0.0.1:5000/ in your browser.

## Deployment

The application is deployed on Render and connected to the GitHub repository.

**Live URL:** https://trekking-management-application-sjfe.onrender.com/

### Automatic Deployment Workflow

1. Make changes to the project locally.
2. Stage and commit the changes using Git.
3. Push the commits to the GitHub `main` branch.
4. Render detects the push and deploys the updated application when automatic deployments are enabled and the build succeeds.

### Render Configuration

- **Runtime:** Python 3
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`
- **Required Environment Variables:** `SECRET_KEY`, `ADMIN_USERNAME`, `ADMIN_PASSWORD`

The website retains its configured Render URL across normal deployments.

**Database note:** The current application uses SQLite. Render's ephemeral filesystem is not suitable for guaranteeing persistent database records across restarts and deployments. Use a persistent database solution before relying on the application for important bookings or user data.

## Future Improvements

- Persistent PostgreSQL database
- Responsive UI improvements
- Enhanced booking workflows
- Improved form validation and error handling
- Additional security and production-readiness improvements

## Author

**DC-Hub753**

GitHub: https://github.com/DC-Hub753/Trekking-Management-Application