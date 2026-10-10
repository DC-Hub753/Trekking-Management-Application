import os
from functools import wraps

from flask import flash, redirect, url_for
from flask_login import LoginManager, login_required, current_user


# -----------------------------
# Database Configuration
# -----------------------------

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, 'instance', 'trekking.db')


# -----------------------------
# Flask-Login
# -----------------------------

login_manager = LoginManager()

login_manager.login_view = "login"


# -----------------------------
# Role Protection
# -----------------------------

def admin_required(f):

    @wraps(f)
    @login_required
    def decorated_function(*args, **kwargs):

        if current_user.__class__.__name__ != "Admin":

            flash("Admin access required.", "danger")

            return redirect(url_for("home"))

        return f(*args, **kwargs)

    return decorated_function


def staff_required(f):

    @wraps(f)
    @login_required
    def decorated_function(*args, **kwargs):

        if current_user.__class__.__name__ != "Staff":

            flash("Staff access required.", "danger")

            return redirect(url_for("home"))

        return f(*args, **kwargs)

    return decorated_function


def user_required(f):

    @wraps(f)
    @login_required
    def decorated_function(*args, **kwargs):

        if current_user.__class__.__name__ != "User":

            flash("User access required.", "danger")

            return redirect(url_for("home"))

        return f(*args, **kwargs)

    return decorated_function