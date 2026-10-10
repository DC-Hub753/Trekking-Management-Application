from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from models import db, Admin, User, Staff
from config import login_manager


# -----------------------------
# User Loader
# -----------------------------

@login_manager.user_loader
def load_user(user_id):

    role, id = user_id.split("-")

    if role == "admin":
        return Admin.query.get(int(id))

    elif role == "user":
        return User.query.get(int(id))

    elif role == "staff":
        return Staff.query.get(int(id))

    return None


# -----------------------------
# User Registration
# -----------------------------

def register_user():

    if request.method == "POST":

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:

            flash("Email already registered!", "danger")

            return redirect(url_for('register_user'))

        new_user = User(
            name=name,
            email=email,
            phone=phone,
            password=generate_password_hash(password)
        )

        db.session.add(new_user)

        db.session.commit()

        flash(
            "Registration Successful! Please Login.",
            "success"
        )

        return redirect(url_for('login'))

    return render_template("register_user.html")


# -----------------------------
# Staff Registration
# -----------------------------

def register_staff():

    if request.method == "POST":

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']

        existing_staff = Staff.query.filter_by(
            email=email
        ).first()

        if existing_staff:

            flash("Email already registered!", "danger")

            return redirect(url_for('register_staff'))

        new_staff = Staff(
            name=name,
            email=email,
            phone=phone,
            password=generate_password_hash(password)
        )

        db.session.add(new_staff)

        db.session.commit()

        flash(
            "Registration Sent! Wait for Admin Approval.",
            "success"
        )

        return redirect(url_for('login'))

    return render_template("register_staff.html")


# -----------------------------
# Login
# -----------------------------

def login():

    if request.method == "POST":

        username = request.form["email"]
        password = request.form["password"]

        # ---------- ADMIN ----------

        admin = Admin.query.filter_by(
            username=username
        ).first()

        if admin and check_password_hash(
            admin.password,
            password
        ):

            login_user(admin)

            flash("Welcome Admin!", "success")

            return redirect(
                url_for("admin_dashboard")
            )

        # ---------- USER ----------

        user = User.query.filter_by(
            email=username
        ).first()

        if user:

            if user.is_blacklisted:

                flash(
                    "Your account has been blacklisted.",
                    "danger"
                )

                return redirect(url_for("login"))

            if check_password_hash(
                user.password,
                password
            ):

                login_user(user)

                flash(
                    "Login Successful!",
                    "success"
                )

                return redirect(
                    url_for("user_dashboard")
                )

        # ---------- STAFF ----------

        staff = Staff.query.filter_by(
            email=username
        ).first()

        if staff:

            if staff.blacklisted:

                flash(
                    "You are blacklisted.",
                    "danger"
                )

                return redirect(url_for("login"))

            if not staff.approved:

                flash(
                    "Waiting for Admin Approval.",
                    "warning"
                )

                return redirect(url_for("login"))

            if check_password_hash(
                staff.password,
                password
            ):

                login_user(staff)

                flash(
                    "Login Successful!",
                    "success"
                )

                return redirect(
                    url_for("staff_dashboard")
                )

        flash(
            "Invalid Credentials",
            "danger"
        )

    return render_template("login.html")


# -----------------------------
# Logout
# -----------------------------

def logout():

    logout_user()

    flash(
        "Logged Out Successfully",
        "success"
    )

    return redirect(url_for("login"))


# -----------------------------
# Route Registration
# -----------------------------

def register_auth_routes(app):

    app.add_url_rule(
        "/register-user",
        "register_user",
        register_user,
        methods=["GET", "POST"]
    )

    app.add_url_rule(
        "/register-staff",
        "register_staff",
        register_staff,
        methods=["GET", "POST"]
    )

    app.add_url_rule(
        "/login",
        "login",
        login,
        methods=["GET", "POST"]
    )

    app.add_url_rule(
        "/logout",
        "logout",
        logout
    )