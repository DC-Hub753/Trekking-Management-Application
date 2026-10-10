# Trekking Management Application

A web-based trekking management system developed using Flask, SQLAlchemy, SQLite, HTML, CSS, Bootstrap, and JavaScript. The application provides separate interfaces and functionality for administrators, trek staff, and users.

## Features

- **User Authentication:** User registration, login, and profile management.
- **Trek Management:** Create, update, view, search, and filter treks.
- **Booking System:** Book treks, view booking history, and track booking status.
- **Admin Dashboard:** Manage treks, users, staff, and bookings.
- **Staff Management:** Assign staff to treks and manage trek participants.
- **Role-Based Access Control:** Separate functionality for administrators, staff, and users.

## Tech Stack

| Category | Technologies |
|---|---|
| Backend | Python, Flask |
| Database | SQLite |
| ORM | SQLAlchemy / Flask-SQLAlchemy |
| Authentication | Flask-Login |
| Frontend | HTML, CSS, Bootstrap, JavaScript |
| Version Control | Git, GitHub |

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
│   └── ...
├── static/
└── .gitignore
```

## Getting Started

### Prerequisites

- Python 3.10 or a compatible version supported by the project dependencies
- pip

### 1. Clone the repository

```bash
git clone https://github.com/DC-Hub753/Trekking-Management-Application.git
cd Trekking-Management-Application
```

### 2. Create and activate a virtual environment

On Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the application

Configure the required application settings and secret key. Initialize the database using the application's database setup procedure, if required.

### 5. Run the application

```bash
python app.py
```

Open the local URL displayed in the terminal.

## Author

**DC-Hub753**

- GitHub: [DC-Hub753](https://github.com/DC-Hub753)
- Project Repository: [Trekking Management Application](https://github.com/DC-Hub753/Trekking-Management-Application)
