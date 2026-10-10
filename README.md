# Trekking Management Application

A web-based trekking management system built with Flask, SQLAlchemy, SQLite, HTML, CSS, Bootstrap, and JavaScript. The application provides role-based functionality for administrators, trek staff, and users.

## Features

- **User Management:** User registration, login, and profile management.
- **Trek Management:** Create, edit, view, search, and filter treks.
- **Booking System:** Book treks, view booking history, and track booking status.
- **Admin Dashboard:** Manage treks, users, staff, and bookings.
- **Staff Management:** Assign staff to treks and manage participants.
- **Role-Based Access:** Separate functionality for administrators, staff, and users.

## Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite
- **ORM:** Flask-SQLAlchemy / SQLAlchemy
- **Authentication:** Flask-Login
- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Version Control:** Git and GitHub

## Project Structure

```text
Trekking Management App/
├── app.py
├── config.py
├── models.py
├── requirements.txt
├── routes/
│   ├── admin.py
│   ├── auth.py
│   ├── staff.py
│   └── user.py
├── templates/
│   ├── admin/
│   ├── staff/
│   ├── user/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   └── register_user.html
├── static/
└── .gitignore
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/DC-Hub753/Trekking-Management-Application.git
cd Trekking-Management-Application
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the application

Set the required environment variables and configure the database according to the application's configuration. Initialize the database if required by the application.

### 5. Run the application

```bash
python app.py
```

Open the local URL displayed in the terminal.

## Learning Outcomes

- Developing a multi-role Flask web application
- Organizing backend functionality using route modules
- Managing relational data using SQLAlchemy
- Implementing authentication and role-based workflows
- Building interactive web pages with HTML, CSS, Bootstrap, and JavaScript

## Author

**DC-Hub753**

GitHub: [https://github.com/DC-Hub753](https://github.com/DC-Hub753)
