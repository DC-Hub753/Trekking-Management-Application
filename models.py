from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()


# ------------------ Admin ------------------

class Admin(UserMixin, db.Model):
    __tablename__ = "admins"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def get_id(self):
        return f"admin-{self.id}"

# ------------------ Users ------------------

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20))
    is_blacklisted = db.Column(db.Boolean, default=False)

    def get_id(self):
        return f"user-{self.id}"

# ------------------ Staff ------------------

class Staff(UserMixin, db.Model):
    __tablename__ = "staff"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20))

    approved = db.Column(db.Boolean, default=False)
    blacklisted = db.Column(db.Boolean, default=False)


    def get_id(self):
        return f"staff-{self.id}"   

# ------------------ Trek ------------------

class Trek(db.Model):
    __tablename__ = "treks"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    location = db.Column(db.String(100), nullable=False)

    difficulty = db.Column(db.String(20))

    duration = db.Column(db.Integer)

    slots = db.Column(db.Integer)

    start_date = db.Column(db.Date)

    end_date = db.Column(db.Date)

    status = db.Column(db.String(20), default="Open")

    staff_id = db.Column(db.Integer, db.ForeignKey("staff.id"))


# ------------------ Booking ------------------

class Booking(db.Model):
    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    trek_id = db.Column(db.Integer, db.ForeignKey("treks.id"))

    booking_date = db.Column(db.Date)

    status = db.Column(db.String(20), default="Booked")